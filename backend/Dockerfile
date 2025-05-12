FROM python:3.11

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .

# Thêm python-multipart do bạn cần UploadFile
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir python-multipart

# Copy source code sau cùng
COPY . .

ENV PYTHONPATH=/app

EXPOSE 8000

# Chạy bằng uvicorn - sử dụng main:application nếu bạn dùng biến application trong main.py
CMD ["python", "-m", "uvicorn", "main:application", "--host", "0.0.0.0", "--port", "8000"]
