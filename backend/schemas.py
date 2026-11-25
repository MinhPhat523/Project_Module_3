"""
Schema xác thực dữ liệu đầu vào và đầu ra cho Backend API (FastAPI).
Sử dụng thư viện Pydantic để chuẩn hóa dữ liệu theo đúng yêu cầu đề bài (Mục 2.8).
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any


class JobPredictRequest(BaseModel):
    """
    Schema định nghĩa dữ liệu đầu vào (Input Features) phục vụ suy luận mức lương.
    
    Lưu ý:
        - Các trường cụ thể sẽ được cập nhật sau khi nhóm hoàn thành bước 03_Feature_Engineering.ipynb.
        - Ví dụ các trường tiềm năng: số năm kinh nghiệm, cấp bậc, vị trí, công nghệ sở hữu...
    """
    # TODO: Khai báo các biến đặc trưng (Features) cụ thể sau khi chốt mô hình
    pass


class JobPredictResponse(BaseModel):
    """
    Schema định dạng kết quả trả về từ mô hình Machine Learning.
    
    Yêu cầu đề bài (Mục 2.8):
        - Kết quả dự đoán (prediction)
        - Độ tin cậy (confidence / probability)
        - Top features đóng góp quan trọng (Explainability)
    """
    predicted_salary: float = Field(..., description="Mức lương dự đoán (Triệu VNĐ/tháng)")
    confidence_score: Optional[float] = Field(default=None, description="Độ tin cậy của dự báo")
    salary_range_min: Optional[float] = Field(default=None, description="Khoảng lương dự kiến tối thiểu")
    salary_range_max: Optional[float] = Field(default=None, description="Khoảng lương dự kiến tối đa")
    top_features: Optional[Dict[str, float]] = Field(default={}, description="Top đặc trưng đóng góp lớn nhất (SHAP)")
