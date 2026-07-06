#!/usr/bin/env python3
"""Translate Hands-On ML (Géron, 2nd ed.) PDF to editable Vietnamese LaTeX.

Pipeline:
  1. extract   EN + Google-VI PDF -> blocks.json
  2. translate blocks (VI reference seed + term-protected Google Translate)
  3. fix       merge, reclassify, drop code/footnotes/images from blocks.json
  4. export    blocks.json -> main.tex + content.tex
  5. compile   xelatex -> PDF

One command per part (read EN PDF side-by-side; no figures in output):

  python translate_pdf_vi.py --part N --all

Edit vi_latex/<part>/blocks.json (field "vi"), then:

  python translate_pdf_vi.py --part N --fix-existing --export-latex --compile
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import fitz
from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent
BOOK_BASENAME = (
  "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
)
BOOK_TITLE = "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"
# LaTeX \\setcounter{tocdepth}: 1=section … 4=paragraph (see heading_command).
DEFAULT_TOC_DEPTH = 4
# Kinds kept out of blocks.json (không in PDF — xem bản gốc).
OMIT_BLOCK_KINDS = frozenset({"image", "meta", "toc", "code", "caption", "footnote"})

# LaTeX article: \paragraph is run-in by default; titlesec makes level 4--5 block headings.
LATEX_HEADING_STYLE = r"""
\usepackage{titlesec}
\titleformat{\paragraph}[block]{\normalfont\normalsize\bfseries}{\theparagraph}{0.5em}{}
\titlespacing*{\paragraph}{0pt}{2.5ex plus .5ex minus .2ex}{1ex}
\titleformat{\subparagraph}[block]{\normalfont\normalsize\bfseries}{\thesubparagraph}{0.5em}{}
\titlespacing*{\subparagraph}{0pt}{2ex plus .5ex minus .2ex}{1ex}
"""
FULL_EN_PDF = ROOT / f"{BOOK_BASENAME}.pdf"
EN_DIR = ROOT / "ilovepdf_split"
VI_REF_DIR = ROOT / "vi"
OUT_DIR = ROOT / "vi_latex"
CACHE_FILE = ROOT / ".translate_cache_vi.json"

TRANSLATOR = GoogleTranslator(source="en", target="vi")
CACHE: dict[str, str] = {}
CHUNK_SIZE = 4500
SLEEP_SEC = 0.12

SKIP_BLOCK_RE = re.compile(
  r"^(©|Machine Translated by Google|\d{1,3})$",
  re.I,
)
COPYRIGHT_RE = re.compile(r"©\s*(Springer|McGraw-Hill|O'Reilly)", re.I)
# Chú thích cuối trang O'Reilly: "15 The location..."
FOOTNOTE_START_RE = re.compile(r"^\d{1,3}\s+[A-Za-z(\"]")
FOOTNOTE_BOTTOM_Y = 500  # PyMuPDF y: vùng footer trang letter (~792pt)

PROTECT_TERMS: list[str] = [
  "Hands-On Machine Learning",
  "Hands-on Machine Learning", "Hands-On", "Hands-on",
  "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
  "Machine Learning", "machine learning",
  "Aurélien Géron", "Aurelien Geron", "Géron", "Geron",
  "O'Reilly", "O'Reilly Media",
  "scikit-learn", "Scikit-Learn", "sklearn",
  "Keras", "keras", "TensorFlow", "tensorflow", "TF",
  "supervised learning", "Supervised Learning", "Supervised learning",
  "unsupervised learning", "Unsupervised Learning", "Unsupervised learning",
  "semisupervised learning", "Semisupervised Learning", "Semisupervised learning",
  "instance-based learning", "Instance-based Learning", "Instance-based learning",
  "model-based learning", "Model-based Learning", "Model-based learning",
  "deep learning", "Deep Learning",
  "reinforcement learning", "Reinforcement Learning",
  "linear regression", "Linear Regression", "Linear regression",
  "logistic regression", "Logistic Regression", "Logistic regression",
  "polynomial regression", "Polynomial Regression",
  "ridge regression", "Ridge Regression", "Lasso", "lasso", "Elastic Net",
  "principal component analysis", "Principal Component Analysis", "PCA",
  "decision tree", "Decision Tree", "Decision Trees", "decision trees",
  "random forest", "Random Forest", "random forests", "Random Forests",
  "ensemble learning", "Ensemble Learning", "ensemble methods",
  "gradient boosting", "Gradient Boosting", "XGBoost", "xgboost",
  "support vector machine", "Support Vector Machine", "SVM",
  "K-nearest neighbors", "K-Nearest Neighbors", "KNN", "K-NN",
  "cross-validation", "Cross-Validation", "cross validation",
  "training set", "Training Set", "test set", "Test Set",
  "validation set", "Validation Set",
  "bias-variance trade-off", "Bias-Variance Trade-Off",
  "mean squared error", "Mean Squared Error", "MSE",
  "feature", "features", "Feature", "Features",
  "predictor", "predictors", "Predictor", "Predictors",
  "dataset", "datasets", "Dataset", "Datasets",
  "bias", "variance", "Bias", "Variance",
  "overfitting", "Overfitting", "underfitting", "Underfitting",
  "regularization", "Regularization",
  "classification", "Classification", "regression", "Regression",
  "clustering", "Clustering",
  "neural network", "Neural Network", "neural networks", "Neural Networks",
  "deep neural network", "Deep Neural Network", "deep neural networks", "Deep Neural Networks",
  "convolutional neural network", "Convolutional Neural Network", "CNN", "CNNs",
  "recurrent neural network", "Recurrent Neural Network", "RNN", "RNNs",
  "LSTM", "GRU", "GAN", "GANs", "autoencoder", "Autoencoder",
  "transformer", "Transformer", "attention", "Attention",
  "natural language processing", "Natural Language Processing", "NLP",
  "recommender systems", "Recommender Systems",
  "batch normalization", "Batch Normalization",
  "dropout", "Dropout",
  "early stopping", "Early Stopping",
  "hyperparameter", "hyperparameters", "Hyperparameter", "Hyperparameters",
  "hyperparameter tuning", "Hyperparameter Tuning",
  "grid search", "Grid Search", "random search", "Random Search",
  "pipeline", "Pipeline", "pipelines", "Pipelines",
  "estimator", "estimators", "Estimator", "Estimators",
  "model", "models", "Model", "Models",
  "parameter", "parameters", "Parameter", "Parameters",
  "weight", "weights", "Weight", "Weights",
  "epoch", "epochs", "Epoch", "Epochs",
  "batch", "batches", "Batch", "Batches",
  "mini-batch", "mini-batches", "Mini-batch", "Mini-batches",
  "learning rate", "Learning Rate",
  "gradient descent", "Gradient Descent",
  "stochastic gradient descent", "Stochastic Gradient Descent", "SGD",
  "Adam", "RMSprop", "Adagrad",
  "backpropagation", "Backpropagation",
  "activation function", "Activation Function",
  "loss function", "Loss Function", "objective function", "target function",
  "confusion matrix", "Confusion Matrix",
  "precision", "recall", "Precision", "Recall", "F1-score", "ROC", "AUC",
  "NumPy", "numpy", "pandas", "matplotlib", "Seaborn", "seaborn",
  "Python", "python", "Jupyter", "Colab", "notebook", "notebooks",
  "MNIST", "Fashion-MNIST", "CIFAR", "ImageNet",
  "California housing", "Swiss roll",
  "Coursera",
  "training example", "Training Example", "training examples", "Training Examples",
  "training error", "Training Error", "test error", "Test Error",
  "DQN", "policy gradient", "Policy Gradient",
  "word embeddings", "Word Embeddings",
  "t-SNE", "TSNE",
]

HEADING_PROTECT_TERMS: list[str] = [
  "Scikit-Learn", "scikit-learn", "Keras", "TensorFlow",
  "CNN", "RNN", "LSTM", "GRU", "GAN", "PCA", "SVM", "SGD", "Adam",
  "XGBoost", "MNIST", "O'Reilly", "Géron", "Geron",
  "Machine Learning", "machine learning", "Deep Learning", "deep learning",
  "gradient descent", "Gradient Descent", "backpropagation", "Backpropagation",
  "reinforcement learning", "Reinforcement Learning",
]

POST_FIXES: list[tuple[str, str]] = [
  (r"\bhọc máy thống kê\b", "statistical learning"),
  (r"\bHọc máy thống kê\b", "Statistical learning"),
  (r"\bHọc máy Thực hành\b", "Hands-On Machine Learning"),
  (r"\bHọc máy thực hành\b", "Hands-On Machine Learning"),
  (r"\bHọc máy\b", "Machine Learning"),
  (r"\bHọc Máy\b", "Machine Learning"),
  (r"\bđặc trưng\b", "feature"),
  (r"\bĐặc trưng\b", "Feature"),
  (r"\bbiến dự đoán\b", "predictor"),
  (r"\bBiến dự đoán\b", "Predictor"),
  (r"\bthiên vị\b", "bias"),
  (r"\bThiên vị\b", "Bias"),
  (r"\bbiến thiên\b", "variance"),
  (r"\bBiến thiên\b", "Variance"),
  (r"\btrọng số\b", "weight"),
  (r"\bTrọng số\b", "Weight"),
  (r"\bthông số\b", "parameter"),
  (r"\bThông số\b", "Parameter"),
  (r"\bđào tạo\b", "training"),
  (r"\bĐào tạo\b", "Training"),
  (r"\bhuấn luyện\b", "training"),
  (r"\bHuấn luyện\b", "Training"),
  (r"\btập huấn luyện\b", "training set"),
  (r"\bTập huấn luyện\b", "Training set"),
  (r"\btập kiểm tra\b", "test set"),
  (r"\bTập kiểm tra\b", "Test set"),
  (r"\bkiểm tra chéo\b", "cross-validation"),
  (r"\bKiểm tra chéo\b", "Cross-validation"),
  (r"\bmô hình\b", "model"),
  (r"\bMô hình\b", "Model"),
  (r"\btập dữ liệu\b", "dataset"),
  (r"\bTập dữ liệu\b", "Dataset"),
  (r"\bphân loại\b", "classification"),
  (r"\bPhân loại\b", "Classification"),
  (r"\bhồi quy\b", "regression"),
  (r"\bHồi quy\b", "Regression"),
  (r"\bchúng tôi\b", "chúng ta"),
  (r"\bChúng tôi\b", "Chúng ta"),
  (r"\bcủa chúng tôi\b", "của chúng ta"),
  (r"\bCủa chúng tôi\b", "Của chúng ta"),
  (r"\bvectơ\b", "vector"),
  (r"\bVectơ\b", "Vector"),
  (r"\bma trận\b", "matrix"),
  (r"\bMa trận\b", "Matrix"),
  (r"\blấy mẫu lại\b", "resampling"),
  (r"\bLấy mẫu lại\b", "Resampling"),
  (r"\bRe-Sampling\b", "Resampling"),
  (r"\bre-sampling\b", "resampling"),
  (r"\bK-Hàng xóm gần nhất\b", "K-Nearest Neighbors"),
  (r"\bK-hàng xóm gần nhất\b", "K-nearest neighbors"),
  (r"\bthuật toán K-Nearest\b", "K-Nearest Neighbors"),
  (r"\bthực hành\b", "lab"),
  (r"\bThực hành\b", "Lab"),
  (r"\bphòng thí nghiệm\b", "lab"),
  (r"\bPhòng thí nghiệm\b", "Lab"),
  (r"\bclassification là\b", "được phân loại là"),
  (r"\bClassification là\b", "Được phân loại là"),
  (r"\bđược classification là\b", "được phân loại là"),
  (r"\bĐược classification là\b", "Được phân loại là"),
  (r"\bvấn đề classification\b", "classification problem"),
  (r"\bVấn đề classification\b", "Classification problem"),
  (r"\bchiếc wage\b", "wage"),
  (r"\bchiếc model\b", "model"),
  (r"\bbảng điều khiển\b", "panel"),
  (r"\bBảng điều khiển\b", "Panel"),
  (r"\bkhông gian phiên bản\b", "version space"),
  (r"\bKhông gian phiên bản\b", "Version space"),
  (r"\bthiên kiến cảm ứng\b", "inductive bias"),
  (r"\bThiên kiến cảm ứng\b", "Inductive bias"),
  (r"\bhọc dựa trên ví dụ\b", "instance-based learning"),
  (r"\bHọc dựa trên ví dụ\b", "Instance-based learning"),
  (r"\bhọc tăng cường\b", "reinforcement learning"),
  (r"\bHọc tăng cường\b", "Reinforcement learning"),
  (r"\bmã\b", "code"),
  (r"\bMã\b", "Code"),
  (r"\bví dụ training\b", "training example"),
  (r"\bVí dụ training\b", "Training example"),
  (r"\bthuật toán học tập\b", "thuật toán learning"),
  (r"\bThuật toán học tập\b", "Thuật toán learning"),
  (r"\bnhiệm vụ học tập\b", "nhiệm vụ learning"),
  (r"\bNhiệm vụ học tập\b", "Nhiệm vụ learning"),
  (r"\bhypothesis space\b", "không gian giả thuyết"),
  (r"\bHypothesis space\b", "Không gian giả thuyết"),
  (r"\bHypothesis Space\b", "Không gian giả thuyết"),
  (r"\bhypothesis spaces\b", "không gian giả thuyết"),
  (r"\bHypothesis spaces\b", "Không gian giả thuyết"),
  (r"\bobjective function\b", "objective function"),
  (r"\btarget function\b", "target function"),
  (r"\bloss function\b", "loss function"),
  (r"\bevaluation function\b", "evaluation function"),
  (r"\bđộ dốc\b", "gradient"),
  (r"\bĐộ dốc\b", "Gradient"),
  (r"\bđi xuống\b", "descent"),
  (r"\bĐi xuống\b", "Descent"),
  (r"\bgradient đi xuống\b", "gradient descent"),
  (r"\bGradient đi xuống\b", "Gradient descent"),
  (r"\bGradient Đi xuống\b", "Gradient descent"),
  (r"\bgenetic algorithms\b", "thuật toán di truyền"),
  (r"\bGenetic algorithms\b", "Thuật toán di truyền"),
  (r"\bGenetic Algorithms\b", "Thuật toán di truyền"),
  (r"\bgenetic algorithm\b", "thuật toán di truyền"),
  (r"\bGenetic algorithm\b", "Thuật toán di truyền"),
  (r"\bAirTemp\b", "Nhiệt độ không khí"),
  (r"\bWarm\b", "Ấm"),
  (r"\bSky\b", "Bầu trời"),
  (r"\binductive learning\b", "học cảm ứng"),
  (r"\bInductive learning\b", "Học cảm ứng"),
  (r"\bInductive Learning\b", "Học cảm ứng"),
  (r"\bcheckers\b", "cờ caro"),
  (r"\bCheckers\b", "Cờ caro"),
  (r"\boutcome\b", "kết quả"),
  (r"\bOutcome\b", "Kết quả"),
  (r"\boutcomes\b", "kết quả"),
  (r"\bOutcomes\b", "Kết quả"),
  (r"\bresponse\b", "phản hồi"),
  (r"\bResponse\b", "Phản hồi"),
  (r"\bresponses\b", "phản hồi"),
  (r"\bResponses\b", "Phản hồi"),
  (r"\bfunction\b", "hàm"),
  (r"\bFunction\b", "Hàm"),
  (r"\bfunctions\b", "hàm"),
  (r"\bFunctions\b", "Hàm"),
  (r"\bthuật toán di truyền\b", "thuật toán di truyền"),
  (r"\bThuật toán di truyền\b", "Thuật toán di truyền"),
  (r"\bmodels phụ gia tổng quát\b", "generalized additive models"),
  (r"\bModels phụ gia tổng quát\b", "Generalized additive models"),
  (r"\bmodel phụ gia tổng quát\b", "generalized additive model"),
  (r"\bModel hậu cần\b", "logistic model"),
  (r"\bmodel hậu cần\b", "logistic model"),
  (r"\bVịnh ngây thơ\b", "naive Bayes"),
  (r"\bvịnh ngây thơ\b", "naive Bayes"),
  (r"\bcây xanh\b", "trees"),
  (r"\bCây xanh\b", "Trees"),
  (r"\bBộ classification\b", "classifier"),
  (r"\bbộ classification\b", "classifier"),
  (r"\bTài liệu Classification\b", "text classification"),
  (r"\btài liệu classification\b", "text classification"),
  (r"\btrình classification\b", "classifier"),
  (r"\bTrình classification\b", "Classifier"),
  (r"\bPhân tích sinh tồn\b", "survival analysis"),
  (r"\bphân tích sinh tồn\b", "survival analysis"),
  (r"\bChức năng Nguy hiểm\b", "Hazard function"),
  (r"\bchức năng nguy hiểm\b", "hazard function"),
  (r"\bMối nguy hiểm\b", "Hazard"),
  (r"\bmối nguy hiểm\b", "hazard"),
  (r"\bcây sống sót\b", "survival trees"),
  (r"\bCây sống sót\b", "Survival trees"),
  (r"\bHoàn thành matrix\b", "matrix completion"),
  (r"\bhoàn thành matrix\b", "matrix completion"),
  (r"\bclustering nghĩa là K\b", "K-means clustering"),
  (r"\bBỏ học\b", "dropout"),
  (r"\bbỏ học\b", "dropout"),
  (r"\bphương pháp thưa thớt\b", "shrinkage methods"),
  (r"\bPhương pháp thưa thớt\b", "Shrinkage methods"),
  (r"\bLời nói đầu\b", "Lời tựa"),
  (r"\blời nói đầu\b", "lời tựa"),
  (r"\bĐịnh tính Predictors\b", "qualitative predictors"),
  (r"\bđịnh tính predictors\b", "qualitative predictors"),
  (r"\bEstimate f\b", "ước tính f"),
  (r"\bestimate f\b", "ước tính f"),
  (r"\bTại sao lại là ước tính f\b", "Tại sao ước tính f?"),
  (r"\bChúng ta thực hiện ước tính f\b", "Chúng ta ước tính f"),
  (r"\bĐược giám sát so với\b", "Supervised so với"),
  (r"\bđược giám sát\b", "supervised"),
  (r"\bĐược giám sát\b", "Supervised"),
  (r"\bModel tuyến tính tổng quát\b", "generalized linear models"),
  (r"\bmodel tuyến tính tổng quát\b", "generalized linear models"),
  (r"\bModels tuyến tính tổng quát\b", "generalized linear models"),
  (r"\bđóng bao\b", "bagging"),
  (r"\bĐóng bao\b", "Bagging"),
  (r"\bTăng cường\b", "boosting"),
  (r"\btăng cường\b", "boosting"),
  (r"\bMạng một lớp\b", "single-layer network"),
  (r"\bMạng đa lớp\b", "multi-layer network"),
  (r"\bĐiều chỉnh mạng\b", "network tuning"),
  (r"\bđiều chỉnh mạng\b", "network tuning"),
  (r"\bNội suy và giảm dần kép\b", "interpolation and double descent"),
  (r"\bLan truyền ngược\b", "backpropagation"),
  (r"\blan truyền ngược\b", "backpropagation"),
  (r"\bGiảm dần độ dốc ngẫu nhiên\b", "stochastic gradient descent"),
  (r"\bMức độ phù hợp đa biến\b", "multicollinearity"),
  (r"\bPhân tích biệt thức bậc hai\b", "quadratic discriminant analysis"),
  (r"\bphân tích biệt thức bậc hai\b", "quadratic discriminant analysis"),
  (r"\bPhân tích phân biệt tuyến tính\b", "linear discriminant analysis"),
  (r"\bphân tích phân biệt tuyến tính\b", "linear discriminant analysis"),
  (r"\bBình phương nhỏ nhất một phần\b", "partial least squares"),
  (r"\bLoại bỏ một lần\b", "leave-one-out"),
  (r"\bCài đặt Classification\b", "classification setting"),
  (r"\bcài đặt classification\b", "classification setting"),
  (r"\bđầu ra giám sát\b", "supervising output"),
  (r"\bbiến đầu vào\b", "input variables"),
  (r"\bBiến đầu vào\b", "Input variables"),
  (r"\bbiến đầu ra\b", "output variable"),
  (r"\bBiến đầu ra\b", "Output variable"),
  (r"\blần input\b", "lần đầu"),
  (r"\boutput được classification\b", "output được phân loại"),
  (r"\bđược classification hoặc\b", "được phân loại hoặc"),
  (r"\bđược classification\b", "được phân loại"),
  (r"\bĐược classification\b", "Được phân loại"),
  (r"\bđược advanced training\b", "có training nâng cao"),
  (r"\bđược training nâng cao\b", "có training nâng cao"),
  (r"\bcá thể\b", "individual"),
  (r"\bCá thể\b", "Individual"),
  (r"\bđược training\b", "được training"),
  (r"\btraining nâng cao\b", "advanced training"),
  (r"\bTeger K\b", "Cho một số nguyên dương K"),
  (r"\bTeger k\b", "Cho một số nguyên dương K"),
  (r"\bVịnh Bayes\b", "naive Bayes"),
  (r"\bmaxj\b", "max_j"),
  (r"\bPr\(Y = cam\|X\)", "Pr(Y = orange | X)"),
  (r"\bPr\(Y =1\|X = x0\)", "Pr(Y = 1 | X = x_0)"),
  (r"\bPr\(Y = 1\|X = x0\)", "Pr(Y = 1 | X = x_0)"),
  # --- Hands-On ML (Géron) ---
  (r"\bLab Machine Learning\b", "Hands-On Machine Learning"),
  (r"\bHands-on Machine Learning\b", "Hands-On Machine Learning"),
  (r"\bNhà thiết kế nội thất\b", "Interior designer"),
  (r"\bBiên tập viên:\s*Amanda Kersey\b", "Copyeditor: Amanda Kersey"),
  (r"\bMáy biến áp tùy chỉnh\b", "Custom Transformer"),
  (r"\bMáy biến áp\b", "Transformer"),
  (r"\bFeature Chia tỷ lệ\b", "Feature Scaling"),
  (r"\bChia tỷ lệ Feature\b", "Feature Scaling"),
  (r"\bHọc tập biểu diễn\b", "representation learning"),
  (r"\bhọc tập biểu diễn\b", "representation learning"),
  (r"\bHọc tập sáng tạo\b", "generative learning"),
  (r"\bhọc tập sáng tạo\b", "generative learning"),
  (r"\bBộ code hóa tự động\b", "autoencoder"),
  (r"\bbộ code hóa tự động\b", "autoencoder"),
  (r"\bMạng code hóa-giải code\b", "encoder-decoder network"),
  (r"\bMạng code hóa\b", "encoder network"),
  (r"\bTriển khai TensorFlow\b", "TensorFlow Serving"),
  (r"\bTensorFlow Triển khai\b", "TensorFlow Serving"),
  (r"\bTraining và triển khai TensorFlow\b", "training và deploying TensorFlow"),
  (r"\btriển khai TensorFlow của Keras API\b", "implementation Keras API trên TensorFlow"),
  (r"\bsử dụng triển khai TensorFlow của Keras API\b", "dùng Keras API trên TensorFlow (tf.keras)"),
  (r"\btriển khai các chương trình\b", "implement các chương trình"),
  (r"\btriển khai nó trong\b", "áp dụng nó trong"),
  (r"\btriển khai nhiều thuật toán Machine Learning\b", "implement nhiều thuật toán Machine Learning"),
  (r"\bThay vì triển khai các phiên bản\b", "Thay vì tự implement các phiên bản"),
  (r"\btriển khai trong các dự án\b", "áp dụng trong các dự án"),
  (r"\bViệc triển khai riêng\b", "Implementation riêng của"),
  (r"\bcách tiếp cận lab\b", "cách tiếp cận hands-on"),
  (r"\bMicro-soft\b", "Microsoft"),
  (r"\bxvi \| Lời tựa\b", ""),
  (r"\bxvii \| Lời tựa\b", ""),
  (r"\bLớp gộp\b", "merge layer"),
  (r"\bChe giấu\b", "masking"),
  (r"\bParameter kỹ thuật môi trường\b", "environment technical parameters"),
  (r"\bMôi trường TF-Agents\b", "TF-Agents environment"),
  (r"\bngười dùng\b", "user"),
  (r"\bNgười dùng\b", "User"),
  (r"\bSECOND EDITION\b", "Ấn bản thứ hai"),
  (r"\b2nd Edition\b", "Ấn bản thứ hai"),
  (r"\bĐã cập nhật cho\b", "Updated for"),
  (r"\bMạng tích chập\b", "convolutional network"),
  (r"\bMạng đối thủ sáng tạo\b", "generative adversarial network"),
  (r"\bMạng đối thủ\b", "adversarial network"),
  (r"\bMạng nơ-ron\b", "neural network"),
  (r"\bmạng nơ-ron\b", "neural network"),
  (r"\bMạng neuron\b", "neural network"),
  (r"\bĐồ thị TensorFlow\b", "TensorFlow Graphs"),
  (r"\bđồ thị TensorFlow\b", "TensorFlow graphs"),
  (r"\bHộp đen\b", "black box"),
  (r"\bhộp đen\b", "black box"),
  (r"\bTinh chỉnh\b", "tuning"),
  (r"\btinh chỉnh\b", "tuning"),
  (r"\bLưu và khôi phục\b", "save and restore"),
  (r"\bMultilabel Classification\b", "multilabel classification"),
  (r"\bMultioutput Classification\b", "multioutput classification"),
  (r"\b  +", " "),
]

MANUAL_VI_FIXES: dict[str, str] = {
  "p1_b1": "Hands-On Machine Learning với Scikit-Learn, Keras & TensorFlow",
  "p1_b4": "",
  "p1_b7": "Updated for",
  "p1_b8": "TensorFlow 2",
  "p3_b2": "Ấn bản thứ hai",
  "p4_b1": "",
  "p4_b8": "Indexer: Judith McConville | Interior designer: David Futato | Cover designer: Karen Montgomery | Illustrator: Rebecca Demarest",
  "p5_b0": "Mục lục",
  "p18_b13": "• Keras là Deep Learning API cấp cao giúp việc training và chạy neural networks rất đơn giản. Nó có thể chạy trên TensorFlow, Theano hoặc Microsoft Cognitive Toolkit (trước đây gọi là CNTK). TensorFlow đi kèm với",
  "p19_b0": "implementation riêng của API này, gọi là tf.keras, cung cấp hỗ trợ cho một số TensorFlow features nâng cao (ví dụ: khả năng tải dữ liệu hiệu quả).",
}

ORDER_FIXES: list[tuple[str, str]] = [
  (r"Hands-On Machine Learning với Scikit-Learn, Keras & TensorFlow", "Hands-On Machine Learning với Scikit-Learn, Keras và TensorFlow"),
  (r"Training và đánh giá trên Training Set", "training và đánh giá trên training set"),
  (r"Chọn và training Model", "chọn và training model"),
  (r"Tinh chỉnh Model", "tuning model"),
  (r"Phân tích Models tốt nhất", "phân tích các model tốt nhất"),
  (r"Lưu và khôi phục Model", "save and restore model"),
  (r"Neural Networks và Deep Learning", "Neural Networks và Deep Learning"),
  (r"Models đã được training trước", "pretrained models"),
  (r"model đề xuất", "recommender model"),
  (r"user vector", "user vector"),
]

CAMEL_RE = re.compile(r"\b[A-Z][a-zA-Z0-9]*(?:[A-Z][a-z0-9]*)+\b")
MATH_INLINE_RE = re.compile(r"\$[^$]+\$|\\\([^)]+\\\)|\\\[[^\]]+\\\]")
HEADING_NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+(.+)$")
FIGURE_TABLE_RE = re.compile(r"^(FIGURE|TABLE)\s+\d", re.I)
TOC_DOTS_RE = re.compile(r"\.{4,}")
GARBLED_RE = re.compile(r"[\x00-\x08\x0b-\x1f]")
NUMERIC_AXIS_RE = re.compile(r"^[\d\s.\-+−×=*(),/\\]+$")
ROMAN_PAGE_RE = re.compile(r"^(vii|viii|ix|x|xi|xii|xiii|xiv|xv|xvi|xvii|xviii|xix|xx)$", re.I)
STANDALONE_PAGE_NUM_RE = re.compile(r"^\d{1,3}$")
PAGE_HEADER_RE = re.compile(r"^\d{1,3}\s+\d+\.\s+")
PAGE_FOOTER_RE = re.compile(r"^\d+\.\s+.+\s+\d{1,3}$")
SECTION_PAGE_FOOTER_RE = re.compile(r"^\d+\.\d+\s+.+\s+\d{1,3}$")
RUNNING_HEADER_RE = re.compile(
  r"^(?:CHAPTER|CHAFER|CHA\s*PTER|CHAF\s*L?ER|C\s*m\s*\d+)\s+\d+\s+.+\s+\d{1,3}\s*$",
  re.I,
)
MACHINE_LEARNING_RUNNING_HEADER_RE = re.compile(
  r"^\d{1,3}\s+MACHINE\s+LEARNING\s*$",
  re.I,
)
SECTION_NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+(.+)$")
BULLET_START_RE = re.compile(r"^[•·▪▫\-]\s*")
KNOWN_CHAPTER_TITLES = frozenset({
  "preface", "lời tựa", "introduction", "giới thiệu", "contents", "nội dung",
  "index", "chỉ số", "bibliography", "exercises", "bài tập",
})
CHART_LABEL_WORDS = frozenset({
  "age", "wage", "year", "education", "volume", "direction", "degree",
  "error", "training", "test", "down", "up", "today", "yesterday",
  "z1", "z2", "z3", "lag1", "lag2", "lag3", "lag4", "lag5",
  "mpg", "horsepower", "weight", "displacement", "origin",
})


def load_cache() -> None:
  global CACHE
  if CACHE_FILE.exists():
    try:
      CACHE = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
      CACHE = {}


def save_cache() -> None:
  try:
    CACHE_FILE.write_text(
      json.dumps(CACHE, ensure_ascii=False, indent=0),
      encoding="utf-8",
    )
  except OSError as exc:
    print(f"  [warn] cache save failed: {exc}", file=sys.stderr)


def _placeholder(kind: str, idx: int) -> str:
  return f"ZZ{kind}{idx}ZZ"


def protect_with_pattern(
  text: str,
  pattern: re.Pattern[str],
  store: list[tuple[str, str]],
) -> str:
  def repl(match: re.Match[str]) -> str:
    original = match.group(0)
    ph = _placeholder("ID", len(store))
    store.append((ph, original))
    return ph

  return pattern.sub(repl, text)


def protect_terms(text: str) -> tuple[str, list[tuple[str, str]]]:
  store: list[tuple[str, str]] = []
  text = protect_with_pattern(text, CAMEL_RE, store)
  for term in sorted(set(PROTECT_TERMS), key=len, reverse=True):
    pat = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)

    def repl(match: re.Match[str], _term: str = term) -> str:
      original = match.group(0)
      ph = _placeholder("T", len(store))
      store.append((ph, original))
      return ph

    text = pat.sub(repl, text)
  return text, store


def restore_terms(text: str, store: list[tuple[str, str]]) -> str:
  for placeholder, term in store:
    text = text.replace(placeholder, term)
  return text


def apply_post_fixes(text: str) -> str:
  for pattern, replacement in POST_FIXES:
    if "\\" in replacement:
      text = re.sub(pattern, lambda _m, r=replacement: r, text)
    else:
      text = re.sub(pattern, replacement, text)
  text = re.sub(r"ZZT\d+ZZ", "", text)
  text = re.sub(r"ZZID\d+ZZ", "", text)
  return text.strip()


def capitalize_prose(text: str) -> str:
  if not text or text.lstrip().startswith(("$", "\\", "%")):
    return text
  if text and text[0].islower():
    text = text[0].upper() + text[1:]
  text = re.sub(
    r"([.!?]\s+)([a-zàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ])",
    lambda m: m.group(1) + m.group(2).upper(),
    text,
  )
  return text


def polish_text(text: str) -> str:
  text = canonicalize_math_storage(text)
  text = apply_post_fixes(text)
  for pattern, replacement in ORDER_FIXES:
    text = re.sub(pattern, replacement, text)
  text = normalize_math_notation(text)
  text = capitalize_prose(text)
  return text


def map_outside_dollars(text: str, transform) -> str:
  """Apply transform only to prose segments (not inside $...$)."""
  if not text:
    return text
  out: list[str] = []
  i = 0
  while i < len(text):
    if text[i] == "$":
      j = text.find("$", i + 1)
      if j == -1:
        out.append(transform(text[i:]))
        break
      out.append(text[i : j + 1])
      i = j + 1
    else:
      j = text.find("$", i)
      if j == -1:
        out.append(transform(text[i:]))
        break
      out.append(transform(text[i:j]))
      i = j
  return "".join(out)


def canonicalize_math_storage(text: str) -> str:
  """Keep math as plain Pr(...), X_1 in blocks.json — LaTeX only at export."""
  if not text:
    return text
  text = text.replace("\\mid", "|")
  text = re.sub(r"\$\\Pr\(([^)]+)\)\$", r"Pr(\1)", text)
  text = re.sub(r"\$\\max_j\$", "max_j", text)
  text = re.sub(r"\$\\mathrm\{([^}]+)\}\$", r"\1", text)
  text = re.sub(r"\$([A-Za-z])_\{?(\d+)\}?\$", r"\1_\2", text)
  text = re.sub(r"\$x_\{?(\d+)\}?\$", r"x_\1", text)
  text = re.sub(r"\$\$+", "", text)
  return text


def normalize_math_notation(text: str) -> str:
  """Restore subscripts / math symbols mangled by translation."""
  if not text:
    return text

  def transform(segment: str) -> str:
    segment = re.sub(
      r"Pr\(([^)]+)\)",
      lambda m: "Pr(" + _normalize_pr_inner(m.group(1)) + ")",
      segment,
    )
    for letter in ("X", "x", "Y", "N", "K"):
      segment = re.sub(rf"\b{letter}(\d+)\b", rf"{letter}_\1", segment)
    segment = re.sub(r"\bmaxj\b", "max_j", segment)
    return segment

  return map_outside_dollars(text, transform)


def _normalize_pr_inner(inner: str) -> str:
  inner = inner.strip()
  inner = re.sub(r"\s*\|\s*", " | ", inner)
  inner = re.sub(r"([A-Za-z])(\d+)\b", r"\1_\2", inner)
  inner = re.sub(r"\s*=\s*", " = ", inner)
  inner = re.sub(r"\s+", " ", inner)
  return inner.strip()


def protect_segments(text: str) -> tuple[str, list[str]]:
  store: list[str] = []

  def repl(match: re.Match[str]) -> str:
    store.append(match.group(0))
    return _placeholder("S", len(store) - 1)

  patterns = [
    r"\$\$[\s\S]*?\$\$",
    r"\$[^$\n]+\$",
    r"\\\([^)]+\\\)",
    r"\\\[[^\]]+\\\]",
    r"Pr\([^)]+\)",
    r"\\[a-zA-Z]+(?:\{[^}]*\})?",
    r"\b[A-Za-z]_\{?\d+\}?",
    r"\b[A-Za-z]\d+\b",
    r"\([^)]*\|[^)]*\)",
    r"https?://\S+",
    r"doi\.org/\S+",
    r"\b[a-z]+_[a-z0-9_]+\b",
    r"\(\d+\.\d+\)",
    r"\\mathbb\{[^}]+\}",
  ]
  protected = text
  for pat in patterns:
    protected = re.sub(pat, repl, protected)
  return protected, store


def restore_segments(text: str, store: list[str]) -> str:
  for i, seg in enumerate(store):
    text = text.replace(_placeholder("S", i), seg)
  return text


def protect_terms_light(text: str, terms: list[str]) -> tuple[str, list[tuple[str, str]]]:
  store: list[tuple[str, str]] = []
  text = protect_with_pattern(text, CAMEL_RE, store)
  for term in sorted(set(terms), key=len, reverse=True):
    pat = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)

    def repl(match: re.Match[str], _term: str = term) -> str:
      original = match.group(0)
      ph = _placeholder("T", len(store))
      store.append((ph, original))
      return ph

    text = pat.sub(repl, text)
  return text, store


def _is_running_page_header(text: str) -> bool:
  t = text.strip()
  if RUNNING_HEADER_RE.match(t):
    return True
  if MACHINE_LEARNING_RUNNING_HEADER_RE.match(t):
    return True
  if re.match(r"^CHAPTER\s*$", t, re.I):
    return True
  if re.match(r"^(ARTIFICIAL|NEURAL|NETWORKS?)\s*$", t, re.I) and len(t) < 20:
    return True
  if re.match(r"^Chapter\s+\d+.*\d{1,3}\s*$", t, re.I) and len(t) < 90:
    return True
  if re.match(r"^Hands-On Machine Learning.*\d{1,3}\s*$", t, re.I):
    return True
  if re.match(r"^(xvi|xvii|xviii|xix|xx)\s*\|\s*(Preface|Lời tựa)\s*$", t, re.I):
    return True
  return False


def _is_false_heading(text: str) -> bool:
  t = text.strip()
  if BULLET_START_RE.match(t):
    return True
  if re.match(r"^-\d+\b", t):
    return True
  if _is_running_page_header(t):
    return True
  m = SECTION_NUM_RE.match(t)
  if m and len(m.group(2)) > 55 and re.search(r"\s[a-z]", m.group(2)):
    return True
  return False


def _normalize_heading_case(text: str) -> str:
  t = text.strip()
  letters = [c for c in t if c.isalpha()]
  if not letters:
    return t
  upper_ratio = sum(c.isupper() for c in letters) / len(letters)
  if upper_ratio >= 0.75:
    return t.title()
  return t


def translate_text_light(text: str, terms: list[str] | None = None) -> str:
  text = text.strip()
  if not text:
    return text
  cache_key = f"__light__:{text}"
  if cache_key in CACHE:
    return CACHE[cache_key]

  term_store: list[tuple[str, str]] = []
  seg_store: list[str] = []
  protected_terms, term_store = protect_terms_light(text, terms or HEADING_PROTECT_TERMS)
  seg_protected, seg_store = protect_segments(protected_terms)
  try:
    if len(seg_protected) <= CHUNK_SIZE:
      out = TRANSLATOR.translate(seg_protected)
    else:
      parts = []
      for i in range(0, len(seg_protected), CHUNK_SIZE):
        chunk = seg_protected[i : i + CHUNK_SIZE]
        parts.append(TRANSLATOR.translate(chunk))
        time.sleep(SLEEP_SEC)
      out = "".join(parts)
    out = restore_segments(out, seg_store)
    out = restore_terms(out, term_store)
    out = polish_text(out)
    CACHE[cache_key] = out
    time.sleep(SLEEP_SEC)
    return out
  except Exception as exc:
    print(f"  [warn] translate failed: {exc!r}", file=sys.stderr)
    return text


def translate_heading(text: str) -> str:
  text = text.strip()
  m = SECTION_NUM_RE.match(text)
  if m:
    num, title = m.group(1), _normalize_heading_case(m.group(2))
    return polish_text(f"{num} {translate_text_light(title)}")
  return polish_text(translate_text_light(_normalize_heading_case(text)))


def should_merge_blocks(a: dict, b: dict) -> bool:
  if a.get("kind") == "image" or b.get("kind") == "image":
    return False
  if a.get("kind") in {"meta", "toc"} or b.get("kind") in {"meta", "toc"}:
    return False
  en_a = (a.get("en") or "").strip()
  en_b = (b.get("en") or "").strip()
  if not en_a or not en_b:
    return False
  if a.get("kind") == "heading" or b.get("kind") == "heading":
    if not (en_a.endswith("-") or en_b[0].islower()):
      return False
  if en_a.endswith("-"):
    return True
  if en_b[0].islower() and not re.search(r'[.!?:]["\']?\s*$', en_a):
    return True
  return False


def merge_text_blocks(a: dict, b: dict) -> None:
  for field in ("en", "vi", "vi_ref"):
    va = (a.get(field) or "").strip()
    vb = (b.get(field) or "").strip()
    if va and vb:
      if va.endswith("-"):
        a[field] = va[:-1] + vb
      else:
        a[field] = f"{va} {vb}"
    elif vb:
      a[field] = vb
  a["bbox"] = [
    min(a["bbox"][0], b["bbox"][0]),
    min(a["bbox"][1], b["bbox"][1]),
    max(a["bbox"][2], b["bbox"][2]),
    max(a["bbox"][3], b["bbox"][3]),
  ]
  a["max_size"] = max(a.get("max_size", 10), b.get("max_size", 10))
  a["vi"] = ""
  a.pop("vi_source", None)


def merge_fragment_blocks(page_blocks: list[dict]) -> list[dict]:
  merged: list[dict] = []
  for block in page_blocks:
    if block.get("kind") == "image":
      merged.append(block)
      continue
    if merged and should_merge_blocks(merged[-1], block):
      merge_text_blocks(merged[-1], block)
      continue
    merged.append(block)
  return merged


def split_merged_heading_block(block: dict) -> list[dict]:
  text = (block.get("en") or "").strip()
  m = SECTION_NUM_RE.match(text)
  if not m:
    return [block]
  num, rest = m.group(1), m.group(2).strip()
  if len(rest) < 30 or len(rest) > 140:
    return [block]
  # Avoid catastrophic backtracking: find sentence body after ALL-CAPS title.
  mo = re.search(r"\s+([A-Z][a-z][^\n]{14,})$", rest)
  if not mo:
    return [block]
  title_part = rest[: mo.start()].strip()
  body = mo.group(1).strip()
  if not title_part or len(body) < 15:
    return [block]
  letters = [c for c in title_part if c.isalpha()]
  if not letters or sum(c.isupper() for c in letters) / len(letters) < 0.7:
    return [block]
  title = f"{num} {title_part}"
  head = dict(block)
  head["en"] = title
  head["vi"] = ""
  head.pop("vi_source", None)
  head["kind"] = "heading"
  head["heading_depth"] = real_heading_depth(title, block.get("max_size", 12))
  para = dict(block)
  para["id"] = block["id"] + "_b"
  para["kind"] = "paragraph"
  para["heading_depth"] = None
  para["en"] = body
  para["vi"] = ""
  para.pop("vi_source", None)
  para["bbox"] = [block["bbox"][0], block["bbox"][3] - 12, block["bbox"][2], block["bbox"][3]]
  return [head, para]


def _footnote_num(block: dict) -> int:
  text = (block.get("en") or block.get("vi") or "").strip()
  m = re.match(r"^(\d{1,3})\s", text)
  return int(m.group(1)) if m else 0


def _is_standalone_footnote(block: dict) -> bool:
  """Numbered footnote in page footer (small font, bottom bbox)."""
  if block.get("kind") in {"image", "meta", "toc", "code", "caption", "heading"}:
    return False
  text = (block.get("en") or block.get("vi") or "").strip()
  if not text or not FOOTNOTE_START_RE.match(text):
    return False
  if block.get("max_size", 12) > 9.5:
    return False
  bbox = block.get("bbox")
  if not bbox or len(bbox) < 4:
    return False
  return bbox[1] >= FOOTNOTE_BOTTOM_Y


def _is_page_footer_number(block: dict) -> bool:
  """Standalone book page number in PDF footer (e.g. '35', 'xii')."""
  text = (block.get("en") or block.get("vi") or "").strip()
  if not text:
    return False
  if not STANDALONE_PAGE_NUM_RE.match(text) and not ROMAN_PAGE_RE.match(text):
    return False
  bbox = block.get("bbox")
  if bbox and len(bbox) >= 4 and bbox[1] >= FOOTNOTE_BOTTOM_Y:
    return True
  # Small isolated digit block without reliable bbox.
  return STANDALONE_PAGE_NUM_RE.match(text) is not None and block.get("max_size", 12) <= 9.5


def reorder_footnotes_to_page_end(page_blocks: list[dict]) -> list[dict]:
  body: list[dict] = []
  footnotes: list[dict] = []
  for block in page_blocks:
    if _is_standalone_footnote(block):
      block["kind"] = "footnote"
      block["heading_depth"] = None
      footnotes.append(block)
    else:
      body.append(block)
  footnotes.sort(key=lambda b: (_footnote_num(b), b.get("bbox", [0, 0, 0, 0])[1]))
  return body + footnotes


def postprocess_page_blocks(page_blocks: list[dict]) -> list[dict]:
  page_blocks = merge_fragment_blocks(page_blocks)
  out: list[dict] = []
  for block in page_blocks:
    if block.get("kind") == "heading" and _is_false_heading(block.get("en", "")):
      if _is_running_page_header(block.get("en", "")):
        block["kind"] = "meta"
        block["vi"] = ""
      elif BULLET_START_RE.match((block.get("en") or "").strip()):
        block["kind"] = "paragraph"
      else:
        block["kind"] = "paragraph"
      out.append(block)
      continue
    if block.get("kind") == "heading":
      rest = SECTION_NUM_RE.match((block.get("en") or "").strip())
      if rest and len(rest.group(2)) >= 30:
        split = split_merged_heading_block(block)
      else:
        split = [block]
      out.extend(split)
      continue
    out.append(block)
  return reorder_footnotes_to_page_end(out)


def translate_text(text: str) -> str:
  text = text.strip()
  if not text:
    return text
  if text in CACHE:
    return CACHE[text]

  term_protected, term_store = protect_terms(text)
  seg_protected, seg_store = protect_segments(term_protected)
  try:
    if len(seg_protected) <= CHUNK_SIZE:
      out = TRANSLATOR.translate(seg_protected)
    else:
      parts = []
      for i in range(0, len(seg_protected), CHUNK_SIZE):
        chunk = seg_protected[i : i + CHUNK_SIZE]
        parts.append(TRANSLATOR.translate(chunk))
        time.sleep(SLEEP_SEC)
      out = "".join(parts)
    out = restore_segments(out, seg_store)
    out = restore_terms(out, term_store)
    out = polish_text(out)
    CACHE[text] = out
    time.sleep(SLEEP_SEC)
    return out
  except Exception as exc:
    print(f"  [warn] translate failed: {exc!r}", file=sys.stderr)
    return text


def join_block_lines(block: dict) -> str:
  lines: list[str] = []
  for line in block.get("lines", []):
    lines.append("".join(span["text"] for span in line.get("spans", [])))
  parts: list[str] = []
  for line in lines:
    line = line.strip()
    if not line:
      continue
    if parts and parts[-1].endswith("-"):
      parts[-1] = parts[-1][:-1] + line
    else:
      parts.append(line)
  return re.sub(r"\s+", " ", " ".join(parts)).strip()


def _looks_like_dedication_line(text: str) -> bool:
  t = text.strip()
  if re.search(r"\d", t):
    return False
  if re.match(r"^[A-Z][a-z]+,", t):
    return True
  if re.match(r"^[A-Z][a-zA-Z'\-]+ (and |và )[A-Z]", t):
    return True
  if t.endswith(":") and len(t) < 55:
    return True
  return False


def _is_math_fragment(text: str) -> bool:
  t = text.strip()
  if not t or len(t) > 150:
    return False
  if STANDALONE_PAGE_NUM_RE.match(t) or ROMAN_PAGE_RE.match(t):
    return False
  if re.fullmatch(r"[xX][\dTt\.]+", t):
    return True
  if re.fullmatch(r"[−\-+*/=.,\d\sA-Za-z\(\)|\\]+", t) and (
    "=" in t or "|" in t or "\\" in t or re.search(r"Pr\(", t)
  ):
    return len(t) < 80
  if re.fullmatch(r"[−\-+Ee\d\s.]+", t) and len(t) < 12:
    return True
  if t in {"K", "j", "J", "Tối đa", "Tối da", "Hàng xóm"}:
    return True
  if re.match(r"^I\s*N\d+$", t, re.I):
    return True
  if re.search(r"\\mathbb|\\hat|\\sum|_\{", t):
    return True
  return False


def real_heading_depth(text: str, max_size: float) -> int | None:
  """1=section, 2=subsection, 3=subsubsection; None = not a TOC heading."""
  t = text.strip()
  if not t or _is_math_fragment(t) or _is_figure_noise(t) or _is_chart_label(t):
    return None
  if PAGE_HEADER_RE.match(t) or PAGE_FOOTER_RE.match(t) or SECTION_PAGE_FOOTER_RE.match(t):
    return None
  if _is_running_page_header(t):
    return None
  if ROMAN_PAGE_RE.match(t):
    return None
  if _looks_like_dedication_line(t):
    return None
  if FIGURE_TABLE_RE.match(t) or TOC_DOTS_RE.search(t):
    return None
  if re.match(r"^(In lần đầu|First [Pp]rinting)", t):
    return None

  m = re.match(r"^(\d+\.\d+\.\d+)\s+(.+)$", t)
  if m and len(m.group(2).strip()) > 2:
    return 3
  m = re.match(r"^(\d+\.\d+)\s+(.+)$", t)
  if m and len(m.group(2).strip()) > 2:
    return 2
  m = re.match(r"^(\d+)\s+(.+)$", t)
  if m and len(m.group(2).strip()) > 2 and max_size >= 11:
    return 1

  tl = t.lower()
  if max_size >= 14 and any(k in tl for k in KNOWN_CHAPTER_TITLES):
    return 1

  if (
    max_size >= 12.5
    and len(t) < 70
    and not t.endswith(".")
    and t.count(" ") <= 8
    and not re.search(r"[.!?]", t)
    and re.search(r"[A-Za-zà-ỹ]{3,}", t)
  ):
    return 2

  return None


def _is_toc_dump(text: str) -> bool:
  t = text.strip()
  if len(t) < 160:
    return False
  if TOC_DOTS_RE.search(t):
    return True
  if len(re.findall(r"\b\d+\.\d+\s+", t)) >= 4:
    return True
  if len(t) > 250 and len(re.findall(r"\b\d{1,3}\b", t)) >= 8:
    # Đoạn văn có nhiều số (%, thống kê) — không phải dump mục lục.
    if t.count(". ") >= 2 and not TOC_DOTS_RE.search(t):
      return False
    return True
  if t.count("  ") >= 8 and len(re.findall(r"\b\d{1,3}\b", t)) >= 6:
    return True
  return False


def _translate_toc_title(en: str) -> str:
  """Translate TOC line: keep number + dot leaders, translate title segment."""
  t = en.strip()
  if not t:
    return t
  m = re.match(r"^((?:Part|Phần)\s+[IVXLC\d]+[.:]?\s*)", t, re.I)
  prefix = m.group(1) if m else ""
  rest = t[len(prefix) :] if prefix else t
  m = re.match(r"^(\d+(?:\.\d+)*[.:]?\s*)(.+)$", rest)
  if not m:
    return polish_text(translate_text_light(t))
  num, body = m.group(1), m.group(2)
  mo = re.search(r"(\s*\.{3,}.*)$", body)
  if mo:
    title, dots = body[: mo.start()], mo.group(1)
  else:
    title, dots = body, ""
  vi_title = polish_text(translate_text_light(title.strip()))
  return f"{prefix}{num}{vi_title}{dots}".strip()


def apply_manual_vi_fixes(pages: list[dict]) -> int:
  n = 0
  for page in pages:
    for block in page["blocks"]:
      fix = MANUAL_VI_FIXES.get(block.get("id", ""))
      if fix is None:
        continue
      if block.get("vi") != fix:
        block["vi"] = fix
        block["vi_source"] = "manual"
        n += 1
      if fix == "" and block.get("kind") != "meta":
        block["kind"] = "meta"
        n += 1
  return n


def reclassify_toc_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
) -> int:
  n = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if block.get("kind") == "image":
        continue
      en = (block.get("en") or "").strip()
      if not en:
        continue
      new_kind = classify_block(en, block.get("max_size", 10))
      if new_kind == "toc" and block.get("kind") != "toc":
        block["kind"] = "toc"
        block["heading_depth"] = None
        n += 1
  return n


def polish_toc_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
) -> int:
  n = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if block.get("kind") != "toc":
        continue
      en = (block.get("en") or "").strip()
      if not en:
        continue
      vi = (block.get("vi") or "").strip()
      if not vi or vi == en or TOC_DOTS_RE.search(en) and not vi:
        new_vi = _translate_toc_title(en)
        if new_vi and new_vi != vi:
          block["vi"] = new_vi
          block["vi_source"] = "toc_translate"
          n += 1
      elif vi:
        fixed = polish_text(vi)
        if fixed != vi:
          block["vi"] = fixed
          n += 1
  return n


CODE_PROSE_TAIL_RE = re.compile(
  r"^(.+?)\s+(with these two:|as follows:|like this:|below:)\s*$",
  re.I,
)
CODE_LIB_MARKERS = (
  r"sklearn\.", r"pandas\.", r"\bnp\.", r"\bpd\.", r"tensorflow", r"\btf\.",
  r"keras\.", r"plt\.", r"housing\.", r"\.plot\(", r"\.legend\(", r"\.show\(",
  r"\.fit\(", r"\.transform\(", r"\.predict\(", r"\.read_csv\(", r"\.value_counts\(\)",
  r"dtype:", r"sparse matrix", r"array\(\[", r"OrdinalEncoder", r"OneHotEncoder",
  r"LinearRegression", r"KNeighborsRegressor", r"Imputer", r"Pipeline\(",
)
PROSE_INLINE_CODE_RE = re.compile(
  r"^(?P<prose>.+?):\d+\s+(?P<code>(?:housing\.|plt\.|pd\.|np\.|import |from |>>>).+)$",
  re.DOTALL,
)


def _is_code_fragment(text: str) -> bool:
  """Python/REPL/shell snippets — keep English, do not translate."""
  t = text.strip()
  if not t or len(t) > 2500:
    return False
  if t.startswith(">>>") or t.startswith("In ["):
    return True
  if re.match(r"^(import|from)\s+[\w.]+", t):
    return True
  if re.match(r"^(def|class)\s+\w+", t):
    return True
  # housing.plot(...), plt.show(), df.head(), ...
  if re.match(r"^[\w.]+\(", t):
    return True
  if re.search(r"\bimport\s+[\w.]+\s+\w+\s*=", t):
    return True
  # Đoạn văn dài (câu hoàn chỉnh) nhắc code inline — không phải block code.
  if len(t) > 220 and t.count(". ") >= 2:
    return False
  hits = sum(1 for pat in CODE_LIB_MARKERS if re.search(pat, t, re.I))
  if hits >= 2:
    return True
  if hits >= 1 and re.search(r"[\w\]\)]\s*=", t):
    return True
  if not re.search(r"[à-ỹÀ-Ỹ]", t) and len(t) < 600:
    code_sym = len(re.findall(r"[=().\[\]_{}]", t))
    kw = len(re.findall(
      r"\b(?:import|from|def|class|return|self|None|True|False|lambda)\b",
      t,
    ))
    if kw >= 1 and code_sym >= 4:
      return True
    if code_sym >= 10:
      return True
  return False


def _block_is_code(block: dict) -> bool:
  if block.get("kind") == "code":
    return True
  if block.get("vi_source") == "code_en":
    return True
  return _is_code_fragment((block.get("en") or "").strip())


def block_omit_from_json(block: dict) -> bool:
  """Blocks not exported to PDF are dropped from blocks.json."""
  if block.get("kind") in OMIT_BLOCK_KINDS:
    return True
  if _block_is_code(block):
    return True
  if _is_standalone_footnote(block):
    return True
  if _is_page_footer_number(block):
    return True
  return False


def strip_non_content_blocks(pages: list[dict]) -> int:
  removed = 0
  for page in pages:
    kept: list[dict] = []
    for block in page["blocks"]:
      if block_omit_from_json(block):
        removed += 1
      else:
        kept.append(block)
    page["blocks"] = kept
  return removed


def save_blocks_json(blocks_path: Path, data: dict, *, report: bool = True) -> int:
  removed = strip_non_content_blocks(data["pages"])
  blocks_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
  if report and removed:
    print(f"Omitted {removed} non-content block(s) from {blocks_path.name}.")
  return removed


def normalize_code_text(text: str) -> str:
  """Light cleanup when PDF extract merges code lines into one string."""
  t = text.strip()
  m = CODE_PROSE_TAIL_RE.match(t)
  if m:
    t = m.group(1).strip()
  t = re.sub(r"\s*>>>\s*", "\n>>> ", t)
  t = re.sub(r"\s{2,}(?=(?:import|from|def|class|return)\s+)", "\n", t)
  return t.strip()


def classify_block(text: str, max_size: float) -> str:
  text = text.strip()
  if not text:
    return "meta"
  if SKIP_BLOCK_RE.match(text):
    return "meta"
  if SECTION_PAGE_FOOTER_RE.match(text):
    return "meta"
  if _is_running_page_header(text):
    return "meta"
  if GARBLED_RE.search(text):
    return "meta"
  if ROMAN_PAGE_RE.match(text):
    return "meta"
  if NUMERIC_AXIS_RE.match(text) and len(text) < 60:
    return "meta"
  if _is_figure_noise(text):
    return "meta"
  if _is_chart_label(text):
    return "meta"
  if re.match(r"^\d+\.\s+\S+$", text) and len(text) < 35:
    return "meta"
  if FIGURE_TABLE_RE.match(text):
    return "caption"
  if _is_toc_dump(text):
    return "toc"
  if TOC_DOTS_RE.search(text):
    return "toc"
  if re.match(r"^(Table of Contents|Contents)\b", text, re.I):
    return "toc"
  if len(text) > 200 and text.count(". .") + text.count("..") > 8:
    return "toc"
  if _is_code_fragment(text):
    return "code"
  if _is_math_fragment(text):
    return "math"
  if _is_false_heading(text):
    pass
  elif real_heading_depth(text, max_size) is not None:
    return "heading"
  return "paragraph"


def block_heading_depth(block: dict) -> int | None:
  depth = block.get("heading_depth")
  if depth is not None:
    return depth
  text = (block.get("vi") or block.get("en") or "").strip()
  if not text:
    return None
  return real_heading_depth(text, block.get("max_size", 10))


def _is_figure_noise(text: str) -> bool:
  """Scatter markers / plot junk extracted as text (o, Oooo, Ồ, ...)."""
  t = text.strip()
  if not t:
    return True
  if re.fullmatch(r"[oOỒồ\s]+", t):
    return True
  if len(t) < 20 and re.fullmatch(r"[oO\s]+", t):
    return True
  if re.fullmatch(r"[xX]\d+", t):
    return True
  return False


def _is_chart_label(text: str) -> bool:
  t = text.strip()
  if not t or len(t) > 45:
    return False
  if FIGURE_TABLE_RE.match(t):
    return False
  tl = t.lower()
  vi_chart_phrases = (
    "xuống lên", "hướng đi hôm nay", "phần trăm thay đổi",
    "hai ngày trước", "ba ngày trước", "trình độ học vấn",
    "hôm qua", "xác suất dự đoán",
  )
  if len(t) < 40 and any(tl == p or tl.startswith(p) for p in vi_chart_phrases):
    return True
  if re.match(
    r"^(today|yesterday|lag\d|down up|direction|education|age|wage|year|z\d+)",
    tl,
  ):
    return True
  if re.match(r"^percentage change", tl):
    return True
  words = re.findall(r"[A-Za-z0-9]+", tl)
  if not words:
    return False
  if len(words) <= 3 and all(w in CHART_LABEL_WORDS or w.isdigit() for w in words):
    return True
  if len(t) < 25 and re.match(r"^Z\d+$", t, re.I):
    return True
  return False


def reclassify_block_kinds(pages: list[dict]) -> int:
  changed = 0
  for page in pages:
    for block in page["blocks"]:
      if block.get("kind") == "image":
        continue
      en = block.get("en", "").strip()
      if not en:
        continue
      if _is_standalone_footnote(block):
        if block.get("kind") != "footnote":
          block["kind"] = "footnote"
          block["heading_depth"] = None
          changed += 1
        continue
      if _is_code_fragment(en):
        block["kind"] = "code"
        block["vi"] = normalize_code_text(en)
        block["vi_source"] = "code_en"
        block["heading_depth"] = None
        changed += 1
        continue
      new_kind = classify_block(en, block.get("max_size", 10))
      new_depth = real_heading_depth(en, block.get("max_size", 10))
      if new_kind == "heading" and new_depth is None:
        new_kind = "paragraph"
      vi = (block.get("vi") or "").strip()
      if vi and (_is_chart_label(vi) or _is_figure_noise(vi)):
        new_kind = "meta"
      if _is_figure_noise(en):
        new_kind = "meta"
      if _is_code_fragment(en):
        new_kind = "code"
        new_depth = None
      if _is_math_fragment(en) and new_kind == "heading":
        new_kind = "math"
      if vi and _is_math_fragment(vi) and new_kind == "heading":
        new_kind = "math"
      if new_kind != block.get("kind") or new_depth != block.get("heading_depth"):
        block["kind"] = new_kind
        block["heading_depth"] = new_depth
        changed += 1
      elif new_kind == block.get("kind") and new_depth != block.get("heading_depth"):
        block["heading_depth"] = new_depth
        changed += 1
  return changed


def extract_pdf_blocks(pdf_path: Path, lang: str) -> list[dict]:
  doc = fitz.open(pdf_path)
  pages: list[dict] = []
  for page_index, page in enumerate(doc):
    page_blocks: list[dict] = []
    for block_index, block in enumerate(page.get_text("dict")["blocks"]):
      block_id = f"p{page_index + 1}_b{block_index}"
      if block["type"] == 1:
        page_blocks.append(
          {
            "id": block_id,
            "kind": "image",
            "bbox": list(block["bbox"]),
            "image_file": f"figures/{block_id}.png",
          }
        )
        continue

      spans = [
        span
        for line in block.get("lines", [])
        for span in line.get("spans", [])
      ]
      if not spans:
        continue
      text = join_block_lines(block)
      if not text:
        continue
      max_size = max(span.get("size", 10) for span in spans)
      kind = classify_block(text, max_size)
      depth = real_heading_depth(text, max_size) if kind == "heading" else None
      if kind == "heading" and depth is None:
        kind = "paragraph"
      entry: dict = {
        "id": block_id,
        "kind": kind,
        "bbox": list(block["bbox"]),
        "max_size": round(max_size, 1),
        "heading_depth": depth,
      }
      if lang == "en":
        entry["en"] = text
        entry["vi"] = ""
      else:
        entry["vi_ref"] = normalize_vi_ref(text)
        entry["en"] = ""
        entry["vi"] = ""
      page_blocks.append(entry)
    page_blocks = postprocess_page_blocks(page_blocks)
    pages.append({"page": page_index + 1, "blocks": page_blocks})
  doc.close()
  return pages


def normalize_vi_ref(text: str) -> str:
  text = re.sub(r"\s+", " ", text).strip()
  return text


def extract_images(pdf_path: Path, pages: list[dict], figures_dir: Path) -> None:
  figures_dir.mkdir(parents=True, exist_ok=True)
  doc = fitz.open(pdf_path)
  for page_info in pages:
    page = doc[page_info["page"] - 1]
    for block in page_info["blocks"]:
      if block.get("kind") != "image":
        continue
      bbox = fitz.Rect(block["bbox"])
      if bbox.width < 20 or bbox.height < 20:
        continue
      pix = page.get_pixmap(clip=bbox, dpi=150)
      out = figures_dir / f"{block['id']}.png"
      pix.save(out)
  doc.close()


def align_vi_reference(en_pages: list[dict], vi_pages: list[dict]) -> None:
  """Seed vi from Google-translated PDF by page + block order."""
  vi_by_page = {p["page"]: p["blocks"] for p in vi_pages}
  for page in en_pages:
    vi_blocks = vi_by_page.get(page["page"], [])
    vi_text_blocks = [b for b in vi_blocks if b.get("kind") != "image"]
    en_text_idx = 0
    for block in page["blocks"]:
      if block.get("kind") == "image" or block.get("kind") == "meta":
        continue
      if en_text_idx >= len(vi_text_blocks):
        break
      vi_ref = vi_text_blocks[en_text_idx].get("vi_ref", "")
      en_text_idx += 1
      if vi_ref and len(vi_ref) > 3:
        block["vi_ref"] = vi_ref


def should_translate_block(block: dict) -> bool:
  if block.get("kind") in {"image", "meta", "toc", "math", "code", "caption", "footnote"}:
    return False
  en = block.get("en", "").strip()
  if _is_figure_noise(en):
    return False
  return bool(en)


def vi_ref_usable(en: str, vi_ref: str, kind: str = "paragraph") -> bool:
  if not vi_ref or len(vi_ref) < 4:
    return False
  if vi_ref.strip().lower() == "machine translated by google":
    return False
  ratio = len(vi_ref) / max(len(en), 1)
  if ratio < 0.35 or ratio > 2.8:
    return False
  if COPYRIGHT_RE.search(vi_ref):
    return False
  if kind == "heading" and not heading_ref_plausible(en, vi_ref):
    return False
  return True


def heading_ref_plausible(en: str, vi_ref: str) -> bool:
  en_num = re.match(r"^(\d+(?:\.\d+)*)", en.strip())
  vi_num = re.match(r"^(\d+(?:\.\d+)*)", vi_ref.strip())
  if en_num and (not vi_num or en_num.group(1) != vi_num.group(1)):
    return False
  en_words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", en)}
  if en_words and len(en) < 80:
    vi_lower = vi_ref.lower()
    if not any(w in vi_lower for w in en_words):
      return False
  return True


def translate_blocks(
  pages: list[dict],
  use_vi_ref: bool = True,
  page_range: tuple[int, int] | None = None,
  force: bool = False,
) -> None:
  load_cache()
  total = sum(
    1
    for p in pages
    for b in p["blocks"]
    if should_translate_block(b)
    and _page_in_range(p["page"], page_range)
  )
  done = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if not should_translate_block(block):
        continue
      done += 1
      en = block["en"].strip()
      if block.get("vi", "").strip() and not force:
        vi = block["vi"].strip()
        if block.get("kind") == "heading" and en and vi.upper() == en.upper():
          pass
        else:
          print(f"  [{done}/{total}] skip (has vi): {block['id']}")
          continue

      if use_vi_ref and block.get("vi_ref") and vi_ref_usable(
        en, block["vi_ref"], kind=block.get("kind", "paragraph")
      ):
        vi = polish_text(block["vi_ref"])
        block["vi"] = vi
        block["vi_source"] = "google_pdf"
        print(f"  [{done}/{total}] ref: {block['id']}")
      elif block.get("kind") == "heading":
        vi = translate_heading(en)
        block["vi"] = vi
        block["vi_source"] = "translator_heading"
        print(f"  [{done}/{total}] hd: {block['id']}")
      else:
        vi = translate_text(en)
        block["vi"] = vi
        block["vi_source"] = "translator"
        print(f"  [{done}/{total}] tr: {block['id']}")
      if done % 10 == 0:
        save_cache()
  save_cache()


def _page_in_range(page: int, page_range: tuple[int, int] | None) -> bool:
  if page_range is None:
    return True
  return page_range[0] <= page <= page_range[1]


def cleanup_noise_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
) -> int:
  cleaned = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      en = (block.get("en") or "").strip()
      vi = (block.get("vi") or "").strip()
      if _is_figure_noise(en) or _is_figure_noise(vi):
        block["kind"] = "meta"
        block["vi"] = ""
        cleaned += 1
  return cleaned


def fix_code_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
) -> int:
  """Mark code snippets and keep English original in vi."""
  n = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      en = (block.get("en") or "").strip()
      if not en:
        continue
      if block.get("kind") != "code" and _is_code_fragment(en):
        block["kind"] = "code"
      if block.get("kind") != "code":
        continue
      block["heading_depth"] = None
      block["vi"] = normalize_code_text(en)
      block["vi_source"] = "code_en"
      n += 1
  return n


def strip_inline_code_suffixes(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
) -> int:
  """Remove code glued after footnote marker in prose blocks (e.g. ':16 housing.plot(...)')."""
  n = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      en = (block.get("en") or "").strip()
      m = PROSE_INLINE_CODE_RE.match(en)
      if not m:
        continue
      block["en"] = m.group("prose").strip()
      vi = (block.get("vi") or "").strip()
      vm = PROSE_INLINE_CODE_RE.match(vi)
      if vm:
        block["vi"] = vm.group("prose").strip()
      n += 1
  return n


def fix_existing_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
  reclassify: bool = True,
  merge_fragments: bool = True,
  retranslate_headings: bool = True,
) -> None:
  if merge_fragments:
    merged_pages = 0
    for page in pages:
      if not _page_in_range(page["page"], page_range):
        continue
      before = len(page["blocks"])
      page["blocks"] = postprocess_page_blocks(page["blocks"])
      if len(page["blocks"]) != before:
        merged_pages += 1
    if merged_pages:
      print(f"Merged/split blocks on {merged_pages} pages.")
  fn_pages = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    old_ids = [b["id"] for b in page["blocks"]]
    page["blocks"] = reorder_footnotes_to_page_end(page["blocks"])
    if [b["id"] for b in page["blocks"]] != old_ids:
      fn_pages += 1
  if fn_pages:
    print(f"Moved footnotes to page end on {fn_pages} page(s).")
  toc_re = reclassify_toc_blocks(pages, page_range=page_range)
  if toc_re:
    print(f"Reclassified {toc_re} TOC blocks.")
  manual = apply_manual_vi_fixes(pages)
  if manual:
    print(f"Applied {manual} manual vi fixes.")
  if reclassify:
    if page_range is None:
      n = reclassify_block_kinds(pages)
    else:
      subset = [p for p in pages if _page_in_range(p["page"], page_range)]
      n = reclassify_block_kinds(subset)
    print(f"Reclassified {n} blocks.")
  recovered = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      en = (block.get("en") or "").strip()
      if block.get("kind") != "meta" or not en or not _is_math_fragment(en):
        continue
      if _is_page_footer_number(block):
        continue
      vi = (block.get("vi") or "").strip()
      if vi and not _is_math_fragment(vi):
        continue
      block["kind"] = "math"
      if not vi:
        block["vi"] = normalize_math_notation(en)
      recovered += 1
  if recovered:
    print(f"Recovered {recovered} math blocks from meta.")
  cleaned = cleanup_noise_blocks(pages, page_range)
  if cleaned:
    print(f"Cleaned {cleaned} figure-noise blocks (o/O/Ồ/X1...).")
  realigned = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if block.get("kind") != "math":
        continue
      if _is_page_footer_number(block):
        block["kind"] = "meta"
        block["vi"] = ""
        realigned += 1
        continue
      en = (block.get("en") or "").strip()
      vi = (block.get("vi") or "").strip()
      if en and _is_math_fragment(en) and vi and not _is_math_fragment(vi):
        block["vi"] = normalize_math_notation(en)
        realigned += 1
      elif vi and (SECTION_PAGE_FOOTER_RE.match(vi) or PAGE_HEADER_RE.match(vi)):
        if not en or not _is_math_fragment(en):
          block["kind"] = "meta"
          block["vi"] = ""
          realigned += 1
  if realigned:
    print(f"Fixed {realigned} misaligned math/page-header blocks.")
  toc_pol = polish_toc_blocks(pages, page_range=page_range)
  if toc_pol:
    print(f"Polished/translated {toc_pol} TOC blocks.")
  if retranslate_headings:
    load_cache()
    rehd = 0
    for page in pages:
      if not _page_in_range(page["page"], page_range):
        continue
      for block in page["blocks"]:
        if block.get("kind") != "heading":
          continue
        en = (block.get("en") or "").strip()
        vi = (block.get("vi") or "").strip()
        if not en:
          continue
        if not vi or vi.upper() == en.upper() or vi == en:
          block["vi"] = translate_heading(en)
          block["vi_source"] = "translator_heading"
          rehd += 1
    if rehd:
      save_cache()
      print(f"Re-translated {rehd} headings.")
  changed = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if block.get("kind") in {"code", "caption", "footnote"}:
        continue
      vi = block.get("vi", "")
      if not vi:
        continue
      fixed = polish_text(vi)
      if fixed != vi:
        block["vi"] = fixed
        changed += 1
  print(f"Polished {changed} blocks.")
  inline_stripped = strip_inline_code_suffixes(pages, page_range=page_range)
  if inline_stripped:
    print(f"Stripped inline code from {inline_stripped} prose block(s).")
  code_fixed = fix_code_blocks(pages, page_range=page_range)
  if code_fixed:
    print(f"Marked {code_fixed} code blocks (English, no translation).")


def latex_escape_mixed(text: str) -> str:
  """Escape prose but keep $...$ math segments."""
  text = normalize_math_notation(text)
  text = inject_latex_math_delimiters(text)
  out: list[str] = []
  i = 0
  while i < len(text):
    if text[i] == "$":
      j = text.find("$", i + 1)
      if j == -1:
        out.append(latex_escape(text[i:]))
        break
      out.append(text[i : j + 1])
      i = j + 1
    else:
      j = text.find("$", i)
      if j == -1:
        out.append(latex_escape(text[i:]))
        break
      out.append(latex_escape(text[i:j]))
      i = j
  return "".join(out)


def inject_latex_math_delimiters(text: str) -> str:
  """Wrap Pr(...) and letter_subscript tokens in $...$ if not already."""
  if not text:
    return text

  def transform(segment: str) -> str:
    def pr_repl(m: re.Match[str]) -> str:
      inner = m.group(1)
      inner = re.sub(r"\s*\|\s*", lambda _m: " \\mid ", inner)
      inner = re.sub(r"\b([A-Za-z])_(\d+)\b", r"\1_{\2}", inner)
      inner = re.sub(r"(?<!\\mathrm\{)\borange\b", r"\\mathrm{orange}", inner)
      return f"$\\Pr({inner})$"

    segment = re.sub(r"Pr\(([^)]+)\)", pr_repl, segment)

    def subscript_outside(s: str) -> str:
      for letter in ("X", "Y", "N"):
        s = re.sub(rf"\b{letter}_(\d+)\b", rf"${letter}_{{\1}}$", s)
        s = re.sub(rf"\b{letter}(\d+)\b", rf"${letter}_{{\1}}$", s)
      s = re.sub(r"\bx_(\d+)\b", r"$x_{\1}$", s)
      s = re.sub(r"\bmax_j\b", lambda _m: "$\\max_j$", s)
      s = re.sub(r"\by_i\b", lambda _m: "$y_i$", s)
      return s

    return map_outside_dollars(segment, subscript_outside)

  return map_outside_dollars(text, transform)


def format_math_fragment(text: str) -> str:
  text = normalize_math_notation(text.strip())
  text = re.sub(r"\s*\((\d+\.\d+)\)\s*$", "", text)
  text = text.replace("−", "-")
  text = inject_latex_math_delimiters(text)
  if text.startswith("$") and text.endswith("$"):
    return text
  return f"${text}$"


def latex_escape(text: str) -> str:
  replacements = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
  }
  out = []
  for ch in text:
    out.append(replacements.get(ch, ch))
  return "".join(out)


def translation_stats(pages: list[dict]) -> tuple[int, int]:
  total = 0
  translated = 0
  for page in pages:
    for block in page["blocks"]:
      if block.get("kind") in {"image", "meta", "code", "caption", "footnote"}:
        continue
      total += 1
      if (block.get("vi") or "").strip():
        translated += 1
  return translated, total


def heading_command(block: dict) -> tuple[str, str, bool]:
  """Return (latex_cmd, title, starred). Starred = not in TOC.

  heading_depth 1–5 maps to section … subparagraph (LaTeX article class).
  """
  text = (block.get("vi") or "").strip()
  if not text:
    text = (block.get("en") or "").strip()
  depth = block_heading_depth(block)
  m = HEADING_NUM_RE.match(text)
  if m:
    title = m.group(2).strip()
  else:
    title = text.strip()
  if depth is None:
    return "textbf", title, True
  cmd_by_depth = {
    1: "section",
    2: "subsection",
    3: "subsubsection",
    4: "paragraph",
    5: "subparagraph",
  }
  cmd = cmd_by_depth.get(int(depth), "subparagraph")
  return cmd, title, False


def block_to_latex(
  block: dict,
  part_dir: Path,
  allow_en_fallback: bool = False,
  include_images: bool = True,
) -> str:
  kind = block.get("kind")
  if kind == "image":
    if not include_images:
      return f"% [image] {block.get('id', '')}\n"
    img = part_dir / block.get("image_file", "")
    if not img.exists():
      return f"% missing image {block['id']}\n"
    rel = Path(block["image_file"]).as_posix()
    return (
      "\\begin{figure}[ht]\n"
      "\\centering\n"
      f"\\includegraphics[width=0.9\\linewidth]{{{rel}}}\n"
      "\\end{figure}\n\n"
    )
  if kind == "meta":
    note = (block.get("vi") or block.get("en", "")).strip()
    if not note or _is_figure_noise(note):
      return ""
    return f"% {latex_escape(note)}\n"
  if kind == "toc":
    return f"% [muc luc] {block.get('id', '')}\n"

  if _block_is_code(block):
    return f"% [code] {block.get('id', '')}\n"

  if kind == "footnote":
    return f"% [footnote] {block.get('id', '')}\n"

  if kind == "math":
    en = (block.get("en") or "").strip()
    vi = (block.get("vi") or "").strip()
    if vi and (_is_math_fragment(vi) or re.search(r"Pr\(|\\|=|_[{\d]", vi)):
      text = vi
    else:
      text = en
    if not text:
      return ""
    body = format_math_fragment(text)
    if body.startswith("$") and body.endswith("$"):
      body = body[1:-1]
    return f"\\[{body}\\]\n\n"

  vi = (block.get("vi") or "").strip()
  en = (block.get("en") or "").strip()
  if not vi:
    if allow_en_fallback and en:
      text = en
    elif en:
      return (
        f"% TODO DICH {block['id']}\n"
        f"% EN: {latex_escape(en[:240])}{'...' if len(en) > 240 else ''}\n\n"
      )
    else:
      return ""
  else:
    text = vi

  if kind == "heading":
    cmd, title, starred = heading_command(block)
    star = "*" if starred else ""
    if cmd == "textbf":
      return f"\\textbf{{{latex_escape(title)}}}\n\n"
    return f"\\{cmd}{star}{{{latex_escape(title)}}}\n\n"
  if kind == "caption":
    # Không in chú thích hình — xem bản gốc (giống block image/code).
    return f"% [caption] {block.get('id', '')}\n"
  if kind == "paragraph" and "•" in text:
    items = [it.strip() for it in re.split(r"\s*•\s*", text) if it.strip()]
    if len(items) > 1:
      body = "".join(f"\\item {latex_escape_mixed(it)}\n" for it in items)
      return f"\\begin{{itemize}}\n{body}\\end{{itemize}}\n\n"
  return f"{latex_escape_mixed(text)}\n\n"


def clamp_toc_depth(depth: int) -> int:
  return min(max(int(depth), 1), 5)


def effective_toc_depth(meta: dict, cli_depth: int | None = None) -> int:
  """TOC depth: CLI flag > blocks.json toc_depth > DEFAULT_TOC_DEPTH."""
  if cli_depth is not None:
    return clamp_toc_depth(cli_depth)
  return clamp_toc_depth(meta.get("toc_depth", DEFAULT_TOC_DEPTH))


def patch_main_tex_toc_depth(main_tex: Path, toc_depth: int) -> bool:
  """Update secnumdepth/tocdepth in main.tex without full re-export."""
  if not main_tex.exists():
    return False
  depth = clamp_toc_depth(toc_depth)
  text = main_tex.read_text(encoding="utf-8")
  new_text = re.sub(
    r"\\setcounter\{secnumdepth\}\{\d+\}",
    rf"\\setcounter{{secnumdepth}}{{{depth}}}",
    text,
    count=1,
  )
  new_text = re.sub(
    r"\\setcounter\{tocdepth\}\{\d+\}",
    rf"\\setcounter{{tocdepth}}{{{depth}}}",
    new_text,
    count=1,
  )
  if new_text == text:
    return False
  main_tex.write_text(new_text, encoding="utf-8")
  return True


def ensure_main_tex_heading_styles(main_tex: Path) -> bool:
  """Insert titlesec block layout for \\paragraph/\\subparagraph if missing."""
  if not main_tex.exists():
    return False
  text = main_tex.read_text(encoding="utf-8")
  if r"\usepackage{titlesec}" in text:
    return False
  marker = r"\usepackage{graphicx}"
  if marker not in text:
    return False
  insert = marker + "\n" + LATEX_HEADING_STYLE.strip() + "\n"
  main_tex.write_text(text.replace(marker, insert, 1), encoding="utf-8")
  return True


def export_latex(
  part_dir: Path,
  meta: dict,
  allow_en_fallback: bool = False,
  include_toc: bool = True,
  include_images: bool = True,
  toc_depth: int | None = None,
) -> None:
  blocks_path = part_dir / "blocks.json"
  data = json.loads(blocks_path.read_text(encoding="utf-8"))
  pages = data["pages"]
  depth = effective_toc_depth(data, toc_depth)
  if data.get("toc_depth") != depth:
    data["toc_depth"] = depth
    save_blocks_json(blocks_path, data, report=False)
  translated, total = translation_stats(pages)
  missing = total - translated

  if missing > 0 and not allow_en_fallback:
    print(
      f"  [warn] {missing}/{total} blocks chua dich (field 'vi' trong).",
      file=sys.stderr,
    )
    print(
      "  Chay: python translate_pdf_vi.py --part N --translate",
      file=sys.stderr,
    )
  elif missing > 0:
    print(f"  [warn] {missing}/{total} blocks dung ban tieng Anh (fallback).")

  content_lines: list[str] = []
  for page in pages:
    content_lines.append(f"% --- page {page['page']} ---\n")
    for block in page["blocks"]:
      content_lines.append(
        block_to_latex(block, part_dir, allow_en_fallback, include_images)
      )

  content_tex = "".join(content_lines)
  (part_dir / "content.tex").write_text(content_tex, encoding="utf-8")

  title = meta.get("title", BOOK_TITLE)
  toc_block = "\\tableofcontents\n\\newpage\n" if include_toc else ""
  secnum_depth = depth
  toc_depth_val = depth
  main_tex = f"""\\documentclass[12pt,a4paper]{{article}}
\\usepackage[a4paper,margin=2.5cm]{{geometry}}
\\usepackage{{fontspec}}
\\usepackage{{polyglossia}}
\\setdefaultlanguage{{vietnamese}}
\\setotherlanguage{{english}}
\\usepackage{{amsmath,amssymb,amsfonts}}
\\usepackage{{graphicx}}
{LATEX_HEADING_STYLE.strip()}
\\usepackage{{hyperref}}
\\usepackage{{indentfirst}}
\\setcounter{{secnumdepth}}{{{secnum_depth}}}
\\setcounter{{tocdepth}}{{{toc_depth_val}}}

\\title{{{latex_escape(title)} (Tiếng Việt)}}
\\author{{Aurélien Géron — bản dịch chỉnh sửa (2nd ed.)}}
\\date{{\\today}}

\\begin{{document}}
\\maketitle
{toc_block}\\input{{content.tex}}
\\end{{document}}
"""
  (part_dir / "main.tex").write_text(main_tex, encoding="utf-8")
  print(f"Wrote {part_dir / 'main.tex'} and content.tex ({translated}/{total} blocks tieng Viet)")


def compile_latex(
  part_dir: Path,
  min_translated_ratio: float = 0.05,
  toc_depth: int | None = None,
) -> None:
  main = part_dir / "main.tex"
  if not main.exists():
    raise FileNotFoundError(f"Missing {main}; run --export-latex first.")

  blocks_path = part_dir / "blocks.json"
  meta: dict = {}
  if blocks_path.exists():
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    meta = data
    translated, total = translation_stats(data["pages"])
    if total and translated / total < min_translated_ratio:
      raise RuntimeError(
        f"Chi co {translated}/{total} blocks da dich. "
        "Chay --translate truoc khi compile."
      )
  depth = effective_toc_depth(meta, toc_depth)
  if blocks_path.exists() and meta.get("toc_depth") != depth:
    meta["toc_depth"] = depth
    save_blocks_json(blocks_path, meta, report=False)
  if patch_main_tex_toc_depth(main, depth):
    print(f"Patched main.tex tocdepth={depth}")
  if ensure_main_tex_heading_styles(main):
    print("Patched main.tex: paragraph headings on own line (titlesec)")
  pdf = part_dir / "main.pdf"
  for _ in range(2):
    subprocess.run(
      ["xelatex", "-interaction=nonstopmode", "main.tex"],
      cwd=part_dir,
      capture_output=True,
      text=True,
      encoding="utf-8",
      errors="replace",
    )
  if not pdf.exists():
    log = part_dir / "main.log"
    tail = log.read_text(encoding="utf-8", errors="replace")[-2000:] if log.exists() else ""
    print(tail, file=sys.stderr)
    raise RuntimeError("xelatex did not produce main.pdf")
  out_name = part_dir.name + ".pdf"
  shutil.copy2(pdf, part_dir.parent / out_name)
  print(f"PDF: {part_dir.parent / out_name}")


def part_pdf_name(part: int) -> str:
  return f"{BOOK_BASENAME}-{part}.pdf"


def resolve_en_pdf(part: int) -> Path:
  split = EN_DIR / part_pdf_name(part)
  if split.exists():
    return split
  if part == 1 and FULL_EN_PDF.exists():
    return FULL_EN_PDF
  return split


def resolve_vi_ref_pdf(part: int) -> Path:
  split = VI_REF_DIR / part_pdf_name(part)
  if split.exists():
    return split
  if part == 1:
    full = VI_REF_DIR / f"{BOOK_BASENAME}.pdf"
    if full.exists():
      return full
  return split


def part_paths(part: int) -> dict[str, Path]:
  stem = f"{BOOK_BASENAME}-{part}"
  return {
    "en": resolve_en_pdf(part),
    "vi_ref": resolve_vi_ref_pdf(part),
    "out": OUT_DIR / stem,
  }


def run_extract(part: int, include_images: bool = True) -> Path:
  paths = part_paths(part)
  if not paths["en"].exists():
    raise FileNotFoundError(paths["en"])

  part_dir = paths["out"]
  part_dir.mkdir(parents=True, exist_ok=True)
  figures_dir = part_dir / "figures"

  print(f"Extracting EN: {paths['en'].name}")
  en_pages = extract_pdf_blocks(paths["en"], lang="en")
  if include_images:
    extract_images(paths["en"], en_pages, figures_dir)
  else:
    print("  [info] Skipping image extraction (--no-images).")

  if paths["vi_ref"].exists():
    print(f"Extracting VI reference: {paths['vi_ref'].name}")
    vi_pages = extract_pdf_blocks(paths["vi_ref"], lang="vi")
    align_vi_reference(en_pages, vi_pages)
  else:
    print("  [warn] VI reference PDF not found; will translate from EN only.")

  payload = {
    "part": part,
    "title": BOOK_TITLE,
    "source_en": str(paths["en"]),
    "source_vi_ref": str(paths["vi_ref"]) if paths["vi_ref"].exists() else None,
    "pages": en_pages,
  }
  blocks_path = part_dir / "blocks.json"
  save_blocks_json(blocks_path, payload)
  print(f"Wrote {blocks_path} ({sum(len(p['blocks']) for p in en_pages)} blocks)")
  return part_dir


def main() -> None:
  parser = argparse.ArgumentParser(
    description="Translate Hands-On ML (Géron) PDF to Vietnamese LaTeX",
  )
  parser.add_argument("--part", type=int, default=1, help="PDF part number (default: 1)")
  parser.add_argument("--extract", action="store_true", help="Extract blocks from PDFs")
  parser.add_argument("--translate", action="store_true", help="Translate blocks.json")
  parser.add_argument("--export-latex", action="store_true", help="Export blocks.json to LaTeX")
  parser.add_argument("--compile", action="store_true", help="Compile main.tex to PDF (xelatex)")
  parser.add_argument("--all", action="store_true",
                      help="extract + translate + fix-existing + export + compile (no images)")
  parser.add_argument(
    "--fix-existing",
    action="store_true",
    help="Apply post-fixes to existing vi text in blocks.json",
  )
  parser.add_argument(
    "--no-vi-ref",
    action="store_true",
    help="Ignore Google-VI PDF; always use online translator",
  )
  parser.add_argument(
    "--force",
    action="store_true",
    help="Re-translate blocks even if vi is already set",
  )
  parser.add_argument(
    "--page-range",
    type=str,
    default=None,
    help="Only translate/fix pages in range, e.g. 12-20",
  )
  parser.add_argument(
    "--allow-en-fallback",
    action="store_true",
    help="Export/export PDF with English text when vi is missing (not recommended)",
  )
  parser.add_argument(
    "--no-toc",
    action="store_true",
    help="Do not include \\tableofcontents in exported main.tex",
  )
  parser.add_argument(
    "--toc-depth",
    type=int,
    default=None,
    metavar="N",
    help=f"TOC depth 1=section … 4=paragraph (default: blocks.json or {DEFAULT_TOC_DEPTH})",
  )
  parser.add_argument(
    "--with-images",
    action="store_true",
    help="With --all: extract figures and embed in PDF (default: skip images)",
  )
  parser.add_argument(
    "--no-images",
    action="store_true",
    help="Skip figure extraction and omit images from exported LaTeX/PDF",
  )
  parser.add_argument(
    "--no-retranslate-headings",
    action="store_true",
    help="With --fix-existing: skip online re-translation of English headings",
  )
  args = parser.parse_args()

  page_range: tuple[int, int] | None = None
  if args.page_range:
    m = re.match(r"^(\d+)\s*-\s*(\d+)$", args.page_range.strip())
    if not m:
      raise SystemExit("--page-range must look like 12-20")
    page_range = (int(m.group(1)), int(m.group(2)))

  part_dir = part_paths(args.part)["out"]

  if args.all:
    args.extract = args.translate = args.export_latex = args.compile = True
    args.fix_existing = True
    if not args.with_images:
      args.no_images = True
    args.no_retranslate_headings = True

  fix_only = (
    args.fix_existing
    and not args.extract
    and not args.translate
    and not args.export_latex
    and not args.compile
  )

  if not any([args.extract, args.translate, args.export_latex, args.compile, args.fix_existing]):
    parser.print_help()
    print("\nExample: python translate_pdf_vi.py --part 1 --all")
    return

  if args.extract:
    part_dir = run_extract(args.part, include_images=not args.no_images)

  blocks_path = part_dir / "blocks.json"

  if args.translate:
    if not blocks_path.exists():
      part_dir = run_extract(args.part, include_images=not args.no_images)
      blocks_path = part_dir / "blocks.json"
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    print(f"Translating part {args.part}...")
    translate_blocks(
      data["pages"],
      use_vi_ref=not args.no_vi_ref,
      page_range=page_range,
      force=args.force,
    )
    save_blocks_json(blocks_path, data, report=False)

  if args.fix_existing:
    if not blocks_path.exists():
      raise FileNotFoundError(blocks_path)
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    fix_existing_blocks(
      data["pages"],
      page_range=page_range,
      retranslate_headings=not args.no_retranslate_headings,
    )
    save_blocks_json(blocks_path, data)
    if fix_only:
      return

  if args.export_latex:
    if not blocks_path.exists():
      raise FileNotFoundError(blocks_path)
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    export_latex(
      part_dir,
      data,
      allow_en_fallback=args.allow_en_fallback,
      include_toc=not args.no_toc,
      include_images=not args.no_images,
      toc_depth=args.toc_depth,
    )

  if args.compile:
    compile_latex(
      part_dir,
      min_translated_ratio=0.0 if args.allow_en_fallback else 0.05,
      toc_depth=args.toc_depth,
    )


if __name__ == "__main__":
  main()
