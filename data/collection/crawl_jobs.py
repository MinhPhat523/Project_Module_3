"""
Module thu thập dữ liệu tin tuyển dụng IT (Data Collection).
Quy định bắt buộc:
- Bắt buộc tự thu thập (Web Scraping / Gọi Public API). Cấm lấy từ Kaggle / UCI.
- Quy mô tối thiểu: >= 1.000 dòng quan sát và >= 5 đặc trưng có ý nghĩa nghiệp vụ.
- Lưu trữ kết quả thô tại: data/raw/
"""

import os
from typing import List, Dict, Tuple, Optional

RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "raw")


def parse_salary_range(salary_raw: str) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    """
    Bóc tách và chuẩn hóa chuỗi mức lương thô về giá trị số (đơn vị: Triệu VNĐ/tháng).
    
    Tham số:
        salary_raw (str): Chuỗi mức lương từ tin tuyển dụng (ví dụ: '15 - 25 triệu', '$1,000 - $1,500').
        
    Trả về:
        Tuple[float, float, float]: (salary_min, salary_max, salary_avg).
        Trả về (None, None, None) nếu là lương 'Thoả thuận' hoặc không trích xuất được.
        
    Gợi ý kỹ thuật:
        - Dùng Regex bóc tách các con số.
        - Quy đổi USD sang Triệu VNĐ nếu có ký hiệu '$' hoặc 'USD'.
        - salary_avg = (salary_min + salary_max) / 2
    """
    pass


def crawl_job_listings(keyword: str = "IT", max_pages: int = 10) -> List[Dict]:
    """
    Cào dữ liệu danh sách tin tuyển dụng từ các nền tảng việc làm (TopCV, ITviec, VietnamWorks...).
    
    Tham số:
        keyword (str): Từ khóa tìm kiếm công việc (mặc định: 'IT').
        max_pages (int): Số lượng trang cần thu thập.
        
    Trả về:
        List[Dict]: Danh sách các tin tuyển dụng thô (chứa tiêu đề, công ty, lương, địa điểm, JD...).
        
    Gợi ý kỹ thuật:
        - Tận dụng bộ lọc 'Có hiển thị mức lương' trên URL để tránh thu thập bài có lương 'Thỏa thuận'.
        - Dùng Requests bắt Hidden API (XHR/Fetch) hoặc dùng BeautifulSoup / Playwright parse HTML.
    """
    pass


def save_raw_data(data: List[Dict], filename: str = "raw_jobs.csv") -> None:
    """
    Lưu danh sách dữ liệu thô đã thu thập được vào thư mục data/raw/.
    
    Tham số:
        data (List[Dict]): Dữ liệu thu thập.
        filename (str): Tên file lưu trữ (.csv hoặc .json).
    """
    pass


if __name__ == "__main__":
    """
    Điểm thực thi chính (Entry point) khi chạy script cào dữ liệu:
    $ python data/collection/crawl_jobs.py
    """
    pass
