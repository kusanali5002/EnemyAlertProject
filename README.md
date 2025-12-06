# 🤖 Báo cáo Bài tập nhóm Môn Trí tuệ Nhân tạo

**📋 Thông tin:**

- **📚 Môn học:** MAT1207E - Nhập môn Trí tuệ Nhân tạo
- **📅 Học kỳ:** Học kỳ 1 - 2025-2026
- **🏫 Trường:** VNU-HUS (Đại học Quốc gia Hà Nội - Trường Đại học Khoa học Tự nhiên)
- **📝 Tiêu đề:** Nhận diện và cảnh báo kẻ địch mạnh trong Genshin Impact
- **📅 Ngày nộp:** 06/12/2025
- **📄 Báo cáo PDF:** https://github.com/HaianCao/FoodChatbot/blob/main/LaTeX%20Template/main-vi.pdf
- **🖥️ Slide thuyết trình:** https://github.com/HaianCao/FoodChatbot/blob/main/slide.pptx
- **📂 Kho lưu trữ:** https://github.com/kusanali5002/EnemyAlertProject

**👥 Thành viên nhóm:**

| 👤 Họ và tên    | 🆔 Mã sinh viên | 🐙 Tên GitHub | 🛠️ Đóng góp                       |
| --------------- | --------------- | ------------- | --------------------------------- |
| Hà Mạnh Dũng    | 23001845      | @kusanali5002   | Toàn bộ dự án    |


---

## 📑 Giới thiệu

Dự án xây dựng một **trình cảnh báo** có khả năng:

- Nhận diện và cảnh báo chính xác các quái vật nguy hiểm trong Genshin Impact
- Không can thiệp vào mã nguồn của game và không vi phạm chính sách phần mềm gian lận.
- Không gây ảnh hưởng đến chất lượng trải nghiệm của người chơi (gây giật lag, giảm FPS, ...)

Hệ thống sử dụng mô hình **YOLOv8** để xử lý bài toán Object Detection được đặt ra trong dự án.

## ⚙️ Triển khai

### 🔍 Pipeline chính

1. **Thu thập dữ liệu** vào game tìm quái vật và quay video, trích xuất frame để lấy ảnh
2. **Tiền xử lý dữ liệu:** xóa các ảnh không đạt chuẩn, sau đó gắn nhãn và vẽ bounding box cho các đối tượng.
3. **Huấn luyện:** gọi YOLOv8 học dữ liệu đã chuẩn bị
4. **Thiết kế cửa sổ cảnh báo:** tạo cửa sổ cảnh báo đơn giản bằng Python.

### 🛠️ Công nghệ sử dụng
- **Ultralytics YOLOv8** (yolov8s)
- **OpenCV**
- **CUDA**
- **PyTorch**

## 📂 Cấu trúc dự án

```plaintext
EnemyAlertProject/
├── dataset/
|     └── label/     # chứa các nhãn (số lượng đã được lược bớt)
|        ├── data.yaml 
|        ├── extract_frame.py    # trích xuất frame
|        ├── train.py      # train data
|        └── yolov8s.pt    # mô hình
├── result/
|     └──detect/
|        ├── Genshin_Enemy_V1/
|        |    └── weight/     # folder trọng số
|        └── visualization/
├── alert_window/               
│   ├── best.pt      # file kết quả huấn luyện tốt nhất
|   └── alert.py          # file chạy cửa sổ cảnh báo
├── LaTeX Template/      # mẫu báo cáo
├── slide.pptx           # slide báo cáo
├── Genshin Alert Project Report.pdf   # báo cáo
├── Proposed Topic Template.md 
└── README.md            # hướng dẫn sử dụng dự án.
```

## Cài đặt môi trường
- Cài đặt phiên bản **Python 3.10** trở lên
- Chạy các lệnh sau để setup môi trường ảo và cài đặt các công cụ và thư viện cần thiết.

```bash
cd EnemyAlertProject

python -m venv venv

venv\Scripts\activate 

pip install -r requirements.txt
```
- Cài đặt PyTorch GPU cho CUDA 11.8 vì PyTorch 2.x hỗ trợ tốt nhất CUDA 11.8
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```


## Tài liệu tham khảo & Phụ lục

**📚 Tài liệu tham khảo**

- OpenCV Library - Computer Vision and Image Processing in Python
- Genshin Monsters Computer Vision Model and Dataset, [https://universe.roboflow.com/genshin-monsters/genshin-monsters]
- Genshin Impact Enemies Gallery, [https://genshin-impact.fandom.com/wiki/Enemy/List]
- pyttsx3 - Python Text-to-Speech Library
- Glenn Jocher, el at., "Ultralytics YOLOv8", Ultralytics, 2023. [https://github.com/ultralytics]
- Distance-IoU Loss : Faster and Better Learning for Bounding Box, Regression, [https://arxiv.org/abs/1911.08287]

### ✅ Danh sách kiểm tra trước khi nộp

- [x] ✅ Đánh dấu X vào ô để xác nhận hoàn thành
- [x] ✍️ Điền đầy đủ các mục trong mẫu README này
- [x] 📄 Hoàn thiện báo cáo PDF chi tiết theo cấu trúc trên
- [x] 🎨 Tuân thủ định dạng và nội dung theo hướng dẫn giảng viên
- [x] ➕ Thêm các mục riêng của dự án nếu cần
- [x] 🔍 Kiểm tra lại ngữ pháp, diễn đạt và độ chính xác kỹ thuật
- [ ] ⬆️ Tải lên báo cáo PDF, slide trình bày và mã nguồn
- [x] 🧩 Đảm bảo tất cả mã nguồn được tài liệu hóa đầy đủ với bình luận và docstring
- [x] 🔗 Kiểm tra các liên kết và tài liệu tham khảo hoạt động đúng

