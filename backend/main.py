"""
Dịch vụ Backend REST API xây dựng bằng FastAPI.
Yêu cầu đề bài (Mục 2.8):
- Tầng 1: Backend API độc lập, phục vụ suy luận mô hình.
- Nạp file mô hình đã tuần tự hóa từ: backend/model/best_model.joblib
- Cung cấp 2 Endpoint bắt buộc:
    1. GET  /health  : Kiểm tra trạng thái hoạt động của server và mô hình.
    2. POST /predict : Tiếp nhận dữ liệu chuẩn hóa qua Pydantic schema, trả về dự đoán và top features.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import JobPredictRequest, JobPredictResponse

app = FastAPI(
    title="IT Salary Prediction API",
    description="Backend REST API phục vụ suy luận mô hình dự đoán mức lương IT Việt Nam",
    version="1.0.0"
)

# Cấu hình CORS để Frontend (Streamlit/React) có thể gọi API mà không bị chặn
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "best_model.joblib")
model = None


def load_model():
    """
    Hàm nạp file mô hình tối ưu đã serialize (best_model.joblib).
    Được gọi khi server khởi động (startup event).
    """
    pass


@app.on_event("startup")
def startup_event():
    """
    Khởi tạo tài nguyên khi server bắt đầu chạy.
    """
    load_model()


@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Endpoint kiểm tra trạng thái hoạt động của server và mô hình.
    """
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "model_path": MODEL_PATH if os.path.exists(MODEL_PATH) else "Chưa có file best_model.joblib"
    }


@app.post("/predict", tags=["Prediction"])
def predict_salary(request: JobPredictRequest):
    """
    Endpoint tiếp nhận thông tin ứng viên và trả về mức lương dự đoán.
    
    Quy trình xử lý:
        1. Chuyển đổi dữ liệu từ Pydantic schema sang định dạng DataFrame phù hợp với Pipeline.
        2. Đưa qua mô hình đã nạp để suy luận.
        3. Tính toán top features đóng góp (SHAP values).
        4. Trả về kết quả dưới định dạng JSON theo schema JobPredictResponse.
    """
    # TODO: Thực thi logic suy luận khi file model/best_model.joblib đã sẵn sàng
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
