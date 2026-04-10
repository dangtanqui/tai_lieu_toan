# Danh sách học AI – Từ số 0 đến nghiên cứu (Không lặp lại)

*Tài liệu tham khảo để tự học/soạn giáo án. Mỗi chủ đề chỉ xuất hiện **một lần** trong danh sách chính (Phần I).*

---

## Cách sử dụng

1. **Danh sách chính** (Phần I): Liệt kê từng mảng kiến thức **một lần duy nhất**, kèm mức độ và mục tiêu.
2. **Bảng ánh xạ** (Phần II): Tên gọi khác nhau (các khóa/cộng đồng) → mục tương ứng trong danh sách chính.
3. **Lộ trình theo giai đoạn** (Phần III): Thứ tự học từ cơ bản → ứng dụng → nghiên cứu, tham chiếu ID.

Nguyên tắc: nếu bạn đã học xong một ID (ví dụ ML1), **không cần** học lại “tên khác” của nó; chỉ học phần nâng cao khi thật sự khác mục tiêu.

---

# PHẦN I: DANH SÁCH CHÍNH (MỖI CHỦ ĐỀ MỘT LẦN)

## Nhóm 0: Kỹ năng nền (bắt buộc để đi xa)

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
|---|---|---|---|---|
| F0 | **Python cơ bản + môi trường** | 0 | Viết code, chạy notebook, quản lý dự án | Python, pip/venv/conda, Jupyter, typing cơ bản |
| F1 | **Git + tư duy làm dự án** | 0–1 | Làm việc như kỹ sư | git, nhánh, PR, README, tái lập thí nghiệm |
| F2 | **Linux/CLI + Docker (tùy)** | 1 | Chạy pipeline, deploy đơn giản | shell, ssh, docker, file system |

## Nhóm 1: Toán tối thiểu cho AI

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
|---|---|---|---|---|
| M1 | **Đại số tuyến tính (cho ML/DL)** | 1 | Hiểu vector/matrix trong mô hình | norm, inner product, eigen/SVD, projection |
| M2 | **Giải tích + tối ưu cơ bản** | 1 | Hiểu gradient/backprop | đạo hàm nhiều biến, chain rule, Taylor, convexity cơ bản |
| M3 | **Xác suất & thống kê (cho ML)** | 1–2 | Hiểu nhiễu, ước lượng, Bayes | RV, expectation, variance, MLE/MAP, CLT |

## Nhóm 2: Nền tảng Machine Learning cổ điển

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
|---|---|---|---|---|
| ML0 | **Tư duy ML + quy trình** | 1 | Biết làm 1 bài toán end-to-end | train/val/test, leakage, metrics, baseline |
| ML1 | **Supervised learning cơ bản** | 1 | Làm được hồi quy/phân loại | linear/logistic, kNN, Naive Bayes, SVM |
| ML2 | **Tree/Ensemble** | 1–2 | Mạnh trong tabular | decision tree, RF, boosting (XGBoost/LightGBM) |
| ML3 | **Unsupervised + giảm chiều** | 1–2 | Khám phá dữ liệu | k-means, GMM, PCA, t-SNE/UMAP |
| ML4 | **Feature engineering** | 1–2 | Tăng chất lượng mô hình | encoding, scaling, text basics, imbalance |
| ML5 | **Model selection + regularization** | 2 | Tránh overfit, chọn mô hình | CV, bias-variance, L1/L2, early stopping |

## Nhóm 3: Deep Learning (từ cơ bản đến hiện đại)

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
|---|---|---|---|---|
| DL0 | **NN cơ bản** | 1–2 | Hiểu backprop & training | MLP, activations, loss, SGD/Adam |
| DL1 | **CNN cho thị giác** | 2 | Làm CV cơ bản | conv, pooling, augmentation, transfer learning |
| DL2 | **Sequence models** | 2 | Xử lý chuỗi/thời gian | RNN/LSTM/GRU, attention (khái niệm) |
| DL3 | **Transformer nền tảng** | 2–3 | Hiểu LLM/ViT | self-attn, MHA, positional enc, layer norm |
| DL4 | **Optimization & training tricks** | 2–3 | Train ổn định, nhanh | init, LR schedule, batch norm, mixed precision |

## Nhóm 4: Dữ liệu, hệ thống, MLOps (đi làm / sản phẩm)

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
|---|---|---|---|---|
| S1 | **Data engineering tối thiểu** | 1–2 | Thu thập & làm sạch dữ liệu | ETL, schema, parquet, quality checks |
| S2 | **Experiment tracking & reproducibility** | 2 | Làm nghiên cứu/kỹ thuật chuẩn | seeds, logging, W&B/MLflow, configs |
| S3 | **Serving & deployment** | 2 | Đưa model lên dịch vụ | REST/gRPC, batching, latency, monitoring |
| S4 | **MLOps pipeline** | 2–3 | Vận hành mô hình | CI/CD, data drift, model registry |

## Nhóm 5: LLM & GenAI (hướng ứng dụng và hướng nghiên cứu)

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
|---|---|---|---|---|
| LLM0 | **LLM basics** | 2 | Biết LLM hoạt động gì | tokenization, pretrain vs finetune, scaling |
| LLM1 | **Prompting & evaluation** | 2 | Dùng LLM có kiểm soát | prompt patterns, test set, hallucination |
| LLM2 | **RAG** | 2–3 | Làm trợ lý tài liệu | embeddings, retriever, chunking, rerank |
| LLM3 | **Finetuning** | 3 | Tùy biến mô hình | SFT, LoRA/QLoRA, data curation |
| LLM4 | **Alignment** | 3 | Hiểu RLHF/DPO | preference data, reward model, DPO/RLHF |
| LLM5 | **Inference/Systems** | 3–4 | Tối ưu chạy mô hình | KV cache, quantization, vLLM/TensorRT-LLM |

## Nhóm 6: Nền tảng nghiên cứu (đọc paper, làm thí nghiệm)

| ID | Chủ đề | Mức | Mục tiêu | Nội dung chính |
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
