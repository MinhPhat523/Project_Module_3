"""
Giao diện người dùng (Frontend UI) xây dựng bằng Streamlit.
Yêu cầu đề bài (Mục 2.8):
- Tầng 2: Giao diện web độc lập gửi HTTP request đến Backend API.
- Cho phép người dùng nhập dữ liệu mẫu và nhận kết quả trực quan trên màn hình.
- Toàn bộ chu trình từ lúc gửi request đến khi nhận kết quả phải phản hồi trong vòng <= 10 giây.
"""

import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"


def render_sidebar():
    """
    Hiển thị thanh công cụ bên cạnh (Sidebar) để kiểm tra trạng thái kết nối tới Backend API (/health).
    """
    pass


def render_input_form() -> dict:
    """
    Hiển thị form nhập liệu các thông số của ứng viên / vị trí công việc:
    - Số năm kinh nghiệm (slider / number input)
    - Cấp bậc, vị trí làm việc, địa điểm (selectbox)
    - Kỹ năng công nghệ (multiselect)
    
    Trả về:
        dict: Dữ liệu người dùng đã chọn để đóng gói vào payload gửi sang Backend.
    """
    pass


def render_prediction_results(prediction_data: dict):
    """
    Hiển thị trực quan kết quả nhận được từ Backend API:
    - Mức lương dự đoán (kèm khoảng lương min - max)
    - Biểu đồ trực quan top đặc trưng ảnh hưởng nhiều nhất đến mức lương (SHAP Explainability)
    """
    pass


def main():
    """
    Hàm điều phối luồng giao diện chính của ứng dụng Streamlit.
    """
    st.set_page_config(
        page_title="Dự Đoán Mức Lương IT Việt Nam",
        page_icon="💼",
        layout="wide"
    )
    st.title("💼 Hệ Thống Dự Đoán Mức Lương Lập Trình Viên IT")
    st.caption("Kiến trúc phân tầng (2-Tier): Streamlit Frontend + FastAPI Backend REST API")
    st.markdown("---")
    
    # TODO: Hiện thực hóa gọi các hàm render_sidebar, render_input_form và kết nối Backend API
    pass


if __name__ == "__main__":
    main()
