# Sử dụng Python 3.11 làm base image
FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /backend

# Copy các file yêu cầu từ hệ thống local vào container
COPY backend/ .
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install uvicorn

RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Mở port mà FastAPI sẽ chạy
EXPOSE 8000

# Lệnh để chạy ứng dụng FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
