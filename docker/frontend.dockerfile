# Sử dụng Python 3.11 làm base image
FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /frontend

# Copy các file yêu cầu từ hệ thống local vào container
COPY frontend/ . 
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Mở port mà Flask sẽ chạy
EXPOSE 5000

# Lệnh để chạy ứng dụng Flask
CMD ["python3", "app.py"]
