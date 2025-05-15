import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
# Đảm bảo có thể import từ thư mục gốc
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

# Thiết lập đường dẫn import, để các file test khác có thể import được module từ thư mục backend/
# Không chứa test nào, chỉ hỗ trợ các file còn lại chạy đúng.