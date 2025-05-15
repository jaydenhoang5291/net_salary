import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
# Đảm bảo có thể import từ thư mục gốc
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

#cấu hình test chung
