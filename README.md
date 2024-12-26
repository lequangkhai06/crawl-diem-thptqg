# THPTQG 2024 Score Scraper

## Mô tả đề tài

Dự án này cào dữ liệu điểm thi THPTQG 2024 từ trang web chính thức. Nó giúp bạn thu thập dữ liệu, phân tích và xử lý để có được cái nhìn rõ hơn về kết quả thi.

## Yêu cầu

- Python 3.8 trở lên
- Các thư viện cần thiết (cài bặng `pip install -r requirements.txt`):
  - requests
  - pandas

## Cách sử dụng

### Bước 1: Clone repo

```bash
git clone https://github.com/your-username/thptqg-2024-score-scraper.git
cd thptqg-2024-score-scraper
```

### Bước 2: Cài đặt thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

### Bước 3: Cấu hình

Chỉnh sửa file `config.json` để thay đổi các thông tin:
- `base_url`: URL chính thức của trang web kết quả.
- `output_file`: Tên file đầu ra lưu điểm (CSV).

### Bước 4: Chạy chương trình

```bash
python main.py
```

Kết quả sẽ được lưu trong file CSV mà bạn cấu hình ở bước trước.

## Cấu trúc dự án

```
thptqg-2024-score-scraper/
├── main.py         # File chính để chạy chương trình
├── sort.py      # Hàm sắp xếp dữ liệu
├── requirements.txt# Danh sách các thư viện cần thiết
├── README.md       # File hướng dẫn (file này)
```

## Lưu ý

- Hãy đảm bảo rằng bạn tuân thủ các quy định pháp luật và chính sách bảo mật của trang web mà bạn cào dữ liệu.
- Đề xuất dùng với mục đích học thuật hoặc phân tích cá nhân, không sử dụng cho mục đích thương mại.

## Đóng góp

Nếu bạn muốn đóng góp vào dự án, hãy tạo Pull Request hoặc gửi issue để trao đổi ý kiến.
