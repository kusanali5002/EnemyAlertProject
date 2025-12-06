### 🏷️ Tên nhóm
Nhóm 50.

### 📝 Tên dự án
Nhận diện và cảnh báo kẻ địch mạnh theo thời gian thực trong Genshin Impact.

### 👥 Thành viên nhóm
| 👤 Họ và tên 🧑‍🎓  | 🆔 Mã sinh viên 🧾 | 🐙 Tên GitHub 🔗     |
|------------------|---------------------|---------------------|
|   Hà Mạnh Dũng   |       23001845      |    @kusanali5002    |

### 🗒️ Tóm tắt
Dự án "AI cảnh báo kẻ địch mạnh theo thời gian thực trong Genshin Impact" nhằm xây dựng một hệ thống hỗ trợ người chơi (đặc biệt là người chơi mới) trong Genshin Impact bằng cách tự động nhắc nhở người chơi khi có kẻ địch mạnh ở gần thông qua việc ứng dụng thị giác máy tính và xử lý hình ảnh thời gian thực. 

### 🎯 Bối cảnh
- Cộng đồng người chơi mới của Genshin ngày càng tăng
- Người chơi mới còn chưa quen thuộc với thế giới cũng như cách hoạt động trong game, dễ dàng bị kẻ địch tấn công hoặc phục kích khi đang thám hiểm, tìm kiếm nguyên liệu hay đơn giản là đang thưởng thức cảnh quan.
- Dự án sẽ giúp người chơi được cảnh báo sớm về kẻ địch xung quanh, từ đó có phản ứng kịp thời

### 🚀 Kế hoạch
# Cách dự định thực hiện dự án 
- Sử dụng mô hình nhận diện vật thể (như Yolov8 chẳng hạn) để phát hiện quái vật trong hình ảnh / video.
- Khi mô hình phát hiện kẻ địch mạnh, phát âm thanh cảnh báo bằng giọng nói
- Chạy thử trên video hoặc trực tiếp từ màn hình khi đang chơi game.
# Các bước chính
- Thu thập dữ liệu : lấy ảnh của kẻ địch hoặc hành vi (hoạt ảnh) nhàn rỗi của chúng từ Hoyowiki và một vài nguồn trên Youtube
- Tiền xử lý dữ liệu : cắt, gắn nhãn và chia dữ liệu thành tập huấn luyện và kiểm thử
- Xây dựng mô hình : Huấn luyện hoặc tinh chỉnh mô hình nhận diện vật thể
- Tích hợp cảnh báo : viết script phát hiện kẻ địch theo thời gian thực và phát âm thanh cảnh báo bằng TTS
- Đánh giá và thử nghiệm : kiểm tra độ chính xác của mô hình cũng như tốc độ nhận diện
- Demo : chạy thử với video gameplay thật để minh họa khả năng phát hiện và cảnh báo của mô hình

### 📚 Tài liệu tham khảo
- OpenCV Library - Computer Vision and Image Processing in Python
- Genshin Monsters Computer Vision Model and Dataset, [https://universe.roboflow.com/genshin-monsters/genshin-monsters]
- Genshin Impact Enemies Gallery, [https://genshin-impact.fandom.com/wiki/Enemy/List]
- pyttsx3 - Python Text-to-Speech Library
