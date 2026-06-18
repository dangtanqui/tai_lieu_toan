# Danh sách học AI – Từ số 0 đến nghiên cứu (Không lặp lại)

*Tài liệu tham khảo để tự học/soạn giáo án. Mỗi chủ đề chỉ xuất hiện **một lần** trong danh sách chính (Phần I).*

---

## Cách sử dụng

1. **Danh sách chính** (Phần I): Liệt kê từng mảng kiến thức **một lần duy nhất**, kèm mức độ và target.
2. **Bảng ánh xạ** (Phần II): Tên gọi khác nhau (các khóa/cộng đồng) → mục tương ứng trong danh sách chính.
3. **Lộ trình theo giai đoạn** (Phần III): Thứ tự học từ cơ bản → ứng dụng → nghiên cứu, tham chiếu ID.

Nguyên tắc: nếu bạn đã học xong một ID (ví dụ ML1), **không cần** học lại “tên khác” của nó; chỉ học phần nâng cao khi thật sự khác target.

---

# PHẦN I: DANH SÁCH CHÍNH (MỖI CHỦ ĐỀ MỘT LẦN)

## Nhóm 0: Kỹ năng nền (bắt buộc để đi xa)

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| F0 | **Python cơ bản + môi trường** | 0 | Viết code, chạy notebook, quản lý dự án | Python, pip/venv/conda, Jupyter, typing cơ bản |
| F1 | **Git + tư duy làm dự án** | 0–1 | Làm việc như kỹ sư | git, nhánh, PR, README, tái lập thí nghiệm |
| F2 | **Linux/CLI + Docker (tùy)** | 1 | Chạy pipeline, deploy đơn giản | shell, ssh, docker, file system |

## Nhóm 1: Toán tối thiểu cho AI

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| M1 | **Đại số tuyến tính (cho ML/DL)** | 1 | Hiểu vector/matrix trong mô hình | norm, inner product, eigen/SVD, projection |
| M2 | **Giải tích + tối ưu cơ bản** | 1 | Hiểu gradient/backprop | đạo hàm nhiều biến, chain rule, Taylor, convexity cơ bản |
| M3 | **Xác suất & thống kê (cho ML)** | 1–2 | Hiểu nhiễu, ước lượng, Bayes | RV, expectation, variance, MLE/MAP, CLT |

## Nhóm 2: Nền tảng Machine Learning cổ điển

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| ML0 | **Tư duy ML + quy trình** | 1 | Biết làm 1 bài toán end-to-end | train/val/test, leakage, metrics, baseline |
| ML1 | **Supervised learning cơ bản** | 1 | Làm được hồi quy/phân loại | linear/logistic, kNN, Naive Bayes, SVM |
| ML2 | **Tree/Ensemble** | 1–2 | Mạnh trong tabular | decision tree, RF, boosting (XGBoost/LightGBM) |
| ML3 | **Unsupervised + giảm chiều** | 1–2 | Khám phá dữ liệu | k-means, GMM, PCA, t-SNE/UMAP |
| ML4 | **Feature engineering** | 1–2 | Tăng chất lượng mô hình | encoding, scaling, text basics, imbalance |
| ML5 | **Model selection + regularization** | 2 | Tránh overfit, chọn mô hình | CV, bias-variance, L1/L2, early stopping |

## Nhóm 3: Deep Learning (từ cơ bản đến hiện đại)

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| DL0 | **NN cơ bản** | 1–2 | Hiểu backprop & training | MLP, activations, loss, SGD/Adam |
| DL1 | **CNN cho thị giác** | 2 | Làm CV cơ bản | conv, pooling, augmentation, transfer learning |
| DL2 | **Sequence models** | 2 | Xử lý chuỗi/thời gian | RNN/LSTM/GRU, attention (khái niệm) |
| DL3 | **Transformer nền tảng** | 2–3 | Hiểu LLM/ViT | self-attn, MHA, positional enc, layer norm |
| DL4 | **Optimization & training tricks** | 2–3 | Train ổn định, nhanh | init, LR schedule, batch norm, mixed precision |

## Nhóm 4: Dữ liệu, hệ thống, MLOps (đi làm / sản phẩm)

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| S1 | **Data engineering tối thiểu** | 1–2 | Thu thập & làm sạch dữ liệu | ETL, schema, parquet, quality checks |
| S2 | **Experiment tracking & reproducibility** | 2 | Làm nghiên cứu/kỹ thuật chuẩn | seeds, logging, W&B/MLflow, configs |
| S3 | **Serving & deployment** | 2 | Đưa model lên dịch vụ | REST/gRPC, batching, latency, monitoring |
| S4 | **MLOps pipeline** | 2–3 | Vận hành mô hình | CI/CD, data drift, model registry |

## Nhóm 5: LLM & GenAI (hướng ứng dụng và hướng nghiên cứu)

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| LLM0 | **LLM basics** | 2 | Biết LLM hoạt động gì | tokenization, pretrain vs finetune, scaling |
| LLM1 | **Prompting & evaluation** | 2 | Dùng LLM có kiểm soát | prompt patterns, test set, hallucination |
| LLM2 | **RAG** | 2–3 | Làm trợ lý tài liệu | embeddings, retriever, chunking, rerank |
| LLM3 | **Finetuning** | 3 | Tùy biến mô hình | SFT, LoRA/QLoRA, data curation |
| LLM4 | **Alignment** | 3 | Hiểu RLHF/DPO | preference data, reward model, DPO/RLHF |
| LLM5 | **Inference/Systems** | 3–4 | Tối ưu chạy mô hình | KV cache, quantization, vLLM/TensorRT-LLM |

## Nhóm 6: Nền tảng nghiên cứu (đọc paper, làm thí nghiệm)

| ID | Chủ đề | Mức | target | Nội dung chính |
|---|---|---|---|---|
| R1 | **Đọc paper & viết báo cáo** | 2–3 | Đọc hiểu, tóm tắt, tái lập | structure, ablation, baseline, repro |
| R2 | **Information theory & generalization (tùy)** | 3 | Cơ sở lý thuyết | entropy, KL, PAC-ish intuition |
| R3 | **Optimization nâng cao (tùy)** | 3 | Hiểu training sâu hơn | convex/nonconvex, GD variants, stability |
| R4 | **Causal inference (tùy)** | 3 | Nhân quả cho KHXH/sản phẩm | DAG, backdoor, IV, A/B testing |
| R5 | **Bayesian & probabilistic modeling (tùy)** | 3–4 | Mô hình hóa bất định | VI, MCMC basics, calibration |

---

# PHẦN II: BẢNG ÁNH XẠ (Tên gọi khác → ID trong danh sách chính)

| Tên gọi ở ngoài | → ID tương ứng |
|---|---|
| “Python for Data Science” | F0 (+ S1 nếu có data) |
| “Math for ML” | M1 + M2 + M3 |
| “ML cơ bản / ML foundations” | ML0 + ML1 + ML2 + ML5 |
| “Data mining” | ML2 + ML3 + ML4 |
| “Deep learning cơ bản” | DL0 + DL1 (+ DL4) |
| “NLP hiện đại” | DL3 (+ LLM0–LLM4) |
| “GenAI / LLM engineering” | LLM1 + LLM2 + LLM5 |
| “MLOps” | S2 + S3 + S4 |
| “AI Research 101” | R1 (+ R3 tùy hướng) |

---

# PHẦN III: LỘ TRÌNH THEO GIAI ĐOẠN (Tham chiếu ID)

## Giai đoạn A — Bắt đầu từ số 0 (4–8 tuần)

- F0, F1  
- M1 (tối thiểu vector/matrix) + M3 (xác suất cơ bản)
- ML0 + ML1 (làm được 1 bài toán classification/regression đơn giản)

## Giai đoạn B — Đi làm dự án (2–4 tháng)

- ML2, ML4, ML5  
- S1, S2 (tối thiểu tracking)  
- DL0 (đủ để đọc hiểu backprop và train NN nhỏ)

## Giai đoạn C — Chuyên DL/LLM (3–6 tháng)

- DL1, DL3, DL4  
- LLM0, LLM1, LLM2 (RAG + evaluation)  
- (tuỳ) LLM3, LLM5 nếu làm fine-tune / inference

## Giai đoạn D — Hướng nghiên cứu (liên tục)

- R1 (thói quen)  
- Chọn nhánh:
  - LLM/GenAI: LLM4 (+ LLM5)  
  - Probabilistic/Bayes: R5  
  - Causal: R4  
  - Optimization: R3

---

## Checklist “đủ nghiên cứu” (tối thiểu)

- Bạn tự tái lập được 1 paper nhỏ (repro) + viết báo cáo ngắn (R1).
- Bạn biết thiết kế ablation + baseline + metric rõ ràng.
- Bạn có pipeline thí nghiệm tái lập (S2) và biết quản lý dữ liệu (S1).

---

# PHẦN IV: SÁCH THAM KHẢO (KÈM LINK PDF MIỄN PHÍ NẾU CÓ)

> Ưu tiên các bản PDF miễn phí/hợp pháp do tác giả công bố. Sách trả phí ghi *(trả phí)*.

## Nhóm 0 – Kỹ năng nền (F0, F1, F2)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Automate the Boring Stuff with Python** | Al Sweigart | [PDF miễn phí](https://automatetheboringstuff.com/) | Python thực hành, rất dễ vào |
| 2 | **Think Python 3e** | Allen B. Downey | [PDF miễn phí](https://greenteapress.com/wp/think-python-3rd-edition/) | Tư duy lập trình qua Python |
| 3 | **Pro Git** | Scott Chacon & Ben Straub | [PDF miễn phí](https://git-scm.com/book/en/v2) | Git từ cơ bản đến nâng cao |
| 4 | **The Missing Semester of Your CS Education** | MIT | [Web miễn phí](https://missing.csail.mit.edu/) | Shell, Git, debugging, profiling |

## Nhóm 1 – Toán cho AI (M1, M2, M3)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Mathematics for Machine Learning** | Deisenroth, Faisal, Ong | [PDF miễn phí](https://mml-book.github.io/) | Đại số tuyến tính + giải tích + xác suất gói gọn cho ML |
| 2 | **Linear Algebra Done Right** | Sheldon Axler | [PDF miễn phí](https://linear.axler.net/) | Đại số tuyến tính chặt chẽ, thiên lý thuyết |
| 3 | **Introduction to Probability** | Blitzstein & Hwang | [PDF bản draft](https://projects.iq.harvard.edu/stat110/home) | Xác suất chuẩn, có bài tập hay |
| 4 | **Convex Optimization** | Boyd & Vandenberghe | [PDF miễn phí](https://web.stanford.edu/~boyd/cvxbook/) | Tối ưu cơ bản → nâng cao, tham khảo khi cần |
| 5 | **The Matrix Cookbook** | Petersen & Pedersen | [PDF miễn phí](https://www.math.uwaterloo.ca/~hwolMDL/matrixcookbook.pdf) | Tra cứu nhanh các công thức matrix |

## Nhóm 2 – Machine Learning cổ điển (ML0–ML5)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **An Introduction to Statistical Learning (ISL)** | James, Witten, Hastie, Tibshirani | [PDF miễn phí](https://www.statlearning.com/) | ML cổ điển dễ hiểu nhất, có bài tập R/Python |
| 2 | **The Elements of Statistical Learning (ESL)** | Hastie, Tibshirani, Friedman | [PDF miễn phí](https://hastie.su.domains/ElemStatLearn/) | Bản nâng cao của ISL, nhiều toán hơn |
| 3 | **Pattern Recognition and Machine Learning (PRML)** | Christopher Bishop | [PDF miễn phí (bản tác giả)](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/) | Kinh điển, nặng Bayesian, rất hay |
| 4 | **Hands-On Machine Learning (3e)** | Aurélien Géron | *(trả phí)* | Thực hành scikit-learn + TF/Keras, rất tốt cho người mới |
| 5 | **Machine Learning: A Probabilistic Perspective** | Kevin Murphy | *(trả phí)* | Toàn diện, nặng xác suất, dùng tham khảo |
| 6 | **Probabilistic Machine Learning: An Introduction** | Kevin Murphy | [PDF bản draft](https://probml.github.io/pml-book/book1.html) | Phiên bản mới/miễn phí của Murphy |
| 7 | **Probabilistic Machine Learning: Advanced Topics** | Kevin Murphy | [PDF bản draft](https://probml.github.io/pml-book/book2.html) | Tập 2 nâng cao |

## Nhóm 3 – Deep Learning (DL0–DL4)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Deep Learning** | Goodfellow, Bengio, Courville | [PDF miễn phí](https://www.deeplearningbook.org/) | "Kinh thánh" DL, lý thuyết chắc |
| 2 | **Dive into Deep Learning (d2l)** | Aston Zhang et al. | [PDF/web miễn phí](https://d2l.ai/) | Lý thuyết + code PyTorch/TF, cập nhật liên tục |
| 3 | **Neural Networks and Deep Learning** | Michael Nielsen | [Web miễn phí](http://neuralnetworksanddeeplearning.com/) | Giải thích trực quan backprop, tốt cho người mới |
| 4 | **Understanding Deep Learning** | Simon J.D. Prince | [PDF miễn phí](https://udlbook.github.io/udlbook/) | Sách mới (2023), hình minh họa đẹp, bao gồm Transformer/Diffusion |
| 5 | **Deep Learning with Python (2e)** | François Chollet | *(trả phí)* | Thực hành Keras, từ tác giả Keras |
| 6 | **The Little Book of Deep Learning** | François Fleuret | [PDF miễn phí](https://fleuret.org/francois/lbdl.html) | Sách bỏ túi ~170 trang, tóm gọn DL hiện đại |

## Nhóm 4 – NLP & Transformer & LLM (DL2, DL3, LLM0–LLM5)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Speech and Language Processing (3e draft)** | Jurafsky & Martin | [PDF miễn phí](https://web.stanford.edu/~jurafsky/slp3/) | NLP kinh điển, cập nhật Transformer/LLM |
| 2 | **Natural Language Processing with Transformers** | Lewis Tunstall et al. | *(trả phí)* | Thực hành HuggingFace Transformers |
| 3 | **Build a Large Language Model (From Scratch)** | Sebastian Raschka | *(trả phí, có repo miễn phí)* — [GitHub](https://github.com/rasbt/LLMs-from-scratch) | Code LLM từ đầu bằng PyTorch |
| 4 | **Attention Is All You Need** (paper) | Vaswani et al. | [PDF](https://arxiv.org/abs/1706.03762) | Paper gốc Transformer, bắt buộc đọc |
| 5 | **The Illustrated Transformer** | Jay Alammar | [Web miễn phí](https://jalammar.github.io/illustrated-transformer/) | Minh họa trực quan Transformer |

## Nhóm 5 – Computer Vision (DL1)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Computer Vision: Algorithms and Applications (2e)** | Richard Szeliski | [PDF miễn phí](https://szeliski.org/Book/) | CV toàn diện, cập nhật DL |
| 2 | **Programming Computer Vision with Python** | Jan Erik Solem | [PDF miễn phí](http://programmingcomputervision.com/) | Thực hành CV bằng Python |

## Nhóm 6 – Reinforcement Learning

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Reinforcement Learning: An Introduction (2e)** | Sutton & Barto | [PDF miễn phí](http://incompleteideas.net/book/the-book-2nd.html) | Sách gốc RL, bắt buộc |
| 2 | **Algorithms for Decision Making** | Kochenderfer et al. | [PDF miễn phí](https://algorithmsbook.com/decisionmaking/) | RL + planning + decision under uncertainty |

## Nhóm 7 – MLOps, Hệ thống & Data (S1–S4)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Designing Machine Learning Systems** | Chip Huyen | *(trả phí)* | MLOps thực tế, rất nên đọc |
| 2 | **Machine Learning Engineering** | Andriy Burkov | [PDF miễn phí](http://www.mlebook.com/) | ML engineering ngắn gọn |
| 3 | **Full Stack Deep Learning** | (course) | [Web miễn phí](https://fullstackdeeplearning.com/) | Khóa học MLOps + production |
| 4 | **Designing Data-Intensive Applications** | Martin Kleppmann | *(trả phí)* | Nền tảng data systems, không chuyên ML nhưng rất quan trọng |

## Nhóm 8 – Nghiên cứu nâng cao (R1–R5)

| # | Tên sách | Tác giả | Link | Ghi chú |
|---|---|---|---|---|
| 1 | **Information Theory, Inference, and Learning Algorithms** | David MacKay | [PDF miễn phí](https://www.inference.org.uk/mackay/itila/) | Information theory + Bayesian, rất hay |
| 2 | **Bayesian Reasoning and Machine Learning** | David Barber | [PDF miễn phí](http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.HomePage) | Bayesian ML chuyên sâu |
| 3 | **Causal Inference in Statistics: A Primer** | Pearl, Glymour, Jewell | *(trả phí)* | Nhân quả nhập môn |
| 4 | **Introduction to Causal Inference** | Brady Neal | [PDF miễn phí](https://www.bradyneal.com/causal-inference-course) | Khóa + notes miễn phí về nhân quả |
| 5 | **Optimization for Machine Learning** | Sra, Nowozin, Wright | [PDF miễn phí](https://arxiv.org/abs/1206.4890) | Tối ưu nâng cao cho ML |
| 6 | **How to Read a Paper** | S. Keshav | [PDF](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) | 3 trang, kỹ năng đọc paper |

---

## Gợi ý thứ tự đọc sách (ánh xạ theo lộ trình Phần III)

| Giai đoạn | Sách ưu tiên |
|---|---|
| **A – Bắt đầu** | Think Python → Mathematics for ML (chương 1–6) → ISL (chương 1–4) |
| **B – Dự án** | Hands-On ML hoặc d2l (phần ML) → ISL (chương 5–10) → ML Engineering |
| **C – DL/LLM** | d2l hoặc Understanding Deep Learning → Jurafsky & Martin (NLP) → LLMs-from-scratch (GitHub) |
| **D – Nghiên cứu** | PRML hoặc Murphy → Deep Learning (Goodfellow) → MacKay → paper chuyên ngành |
