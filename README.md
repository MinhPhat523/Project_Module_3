# Dự Đoán Mức Lương Lập Trình Viên & Phân Tích Thị Trường IT Việt Nam
## End-to-End Machine Learning Pipeline Project

---

## 📌 Giới Thiệu Đề Tài
Đồ án thuộc **Module 3: Data Science & Machine Learning**, nhằm mục đích xây dựng một hệ thống Machine Learning hoàn chỉnh (End-to-End Pipeline) từ thu thập dữ liệu tuyển dụng thực tế, tiền xử lý, huấn luyện các thuật toán hồi quy, giải thích quyết định của mô hình (XAI) cho đến đóng gói dịch vụ Backend API và giao diện Web tương tác trực tiếp cho người dùng.

---

## 📁 Cấu Trúc Thư Mục Tiêu Chuẩn

```text
it-salary-prediction/
  ├── data/
  │   ├── raw/                      # Dữ liệu cào thô (>= 1.000 dòng CSV/JSON)
  │   ├── processed/                # Dữ liệu sạch sau tiền xử lý
  │   └── collection/               # Script cào dữ liệu tuyển dụng
  │
  ├── notebooks/
  │   ├── 01_EDA.ipynb              # Trực quan hóa dữ liệu (>= 5 biểu đồ, >= 3 insights)
  │   ├── 02_Preprocessing.ipynb    # Làm sạch, xử lý missing, outliers, encode, scale
  │   ├── 03_Feature_Engineering.ipynb # Tạo feature mới & lựa chọn đặc trưng
  │   ├── 04_Modeling.ipynb         # Train >= 3 model, đối sánh metric, tuning
  │   └── 05_Explainability.ipynb   # Giải thích mô hình bằng SHAP / LIME
  │
  ├── backend/                    # Dịch vụ Backend REST API
  │   ├── main.py                   # Ứng dụng FastAPI (Endpoints /health, /predict)
  │   ├── schemas.py                # Schema xác thực dữ liệu Pydantic
  │   ├── model/
  │   │   └── best_model.joblib     # File mô hình tối ưu đã serialize
  │   └── requirements.txt          # Thư viện Backend
  │
  ├── frontend/                   # Giao diện người dùng
  │   ├── app.py                    # Giao diện tương tác Streamlit
  │   └── requirements.txt          # Thư viện Frontend
  │
  ├── report/
  │   └── Final_Report.pdf          # Báo cáo chuẩn NCKH 6 phần (6 - 8 trang)
  │
  ├── presentation/
  │   └── Demo_Slides.pdf           # Slide thuyết trình bảo vệ (15 phút)
  │
  ├── .gitignore
  └── README.md
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Hệ Thống

### 1. Khởi tạo môi trường ảo Python
```bash
python3 -m venv venv
source venv/bin/activate  # Trên macOS/Linux
# venv\Scripts\activate   # Trên Windows
```

### 2. Chạy Backend API (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
- Truy cập tài liệu API tự động Swagger UI tại: [http://localhost:8000/docs](http://localhost:8000/docs)
- Endpoint kiểm tra server: [http://localhost:8000/health](http://localhost:8000/health)

### 3. Chạy Frontend UI (Streamlit)
Mở một cửa sổ Terminal mới:
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
- Giao diện web sẽ tự động mở tại: [http://localhost:8501](http://localhost:8501)

---

## 📅 Các Mốc Bàn Giao Quan Trọng
- **30/11:** Nộp Báo cáo tổng quan đề tài.
- **10/12:** Hoàn thành 50% dự án (xong dữ liệu, EDA, Baseline Model).
- **13/01:** Nộp toàn bộ mã nguồn, sản phẩm và Final Report.
- **14/01 – 16/01:** Thuyết trình & Live Demo trước Hội đồng.
