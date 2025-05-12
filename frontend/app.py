import streamlit as st
import pandas as pd
import requests
import io
import os

st.set_page_config(page_title="Net Salary Tool", page_icon="🧾", layout="wide")

# 🔧 Lấy URL API từ biến môi trường (Render: Settings > Environment > API_URL)
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Sidebar Navigation
st.sidebar.title("📋 Chức năng")
page = st.sidebar.radio("Đi tới", ["Tính lương từng người", "Tính lương hàng loạt"])

st.title("💼 Ứng dụng tính lương NET")

# ===== 1. TÍNH LƯƠNG TỪNG NGƯỜI =====
if page == "Tính lương từng người":
    st.subheader("🔹 Nhập thông tin để tính lương")
    gross = st.number_input("👉 Nhập lương GROSS (VND)", step=1_000_000, min_value=0)
    dependents = st.number_input("👨‍👩‍👧‍👦 Số người phụ thuộc", step=1, min_value=0)

    if st.button("📤 Tính toán"):
        try:
            res = requests.post(f"{API_URL}/api/net/single",
                                json={
                                    "gross": gross, 
                                    "dependents": dependents
                                }
                                )
            if res.status_code == 200:
                data = res.json()
                st.success("✅ Tính toán thành công!")

                # Hiển thị kết quả
                df_result = pd.DataFrame({
                    "Thông tin": ["Lương GROSS", "Tiền BH", "Thuế TNCN", "Lương NET"],
                    "Giá trị (VND)": [
                        f"{data['gross_salary']:,.0f}",
                        f"{data['insurance_fee']:,.0f}",
                        f"{data['tax_due']:,.0f}",
                        f"{data['net_salary']:,.0f}"
                    ]
                })
                st.table(df_result)
            else:
                st.error(f"❌ Lỗi từ server: {res.status_code}")
        except Exception as e:
            st.error(f"⚠️ Không kết nối được server: {str(e)}")

# ===== 2. TÍNH LƯƠNG HÀNG LOẠT =====
elif page == "Tính lương hàng loạt":
    st.subheader("📥 Tải file mẫu Excel")

    template_df = pd.DataFrame({
        "Employee ID": [1, 2],
        "Name": ["Nguyễn Văn A", "Trần Thị B"],
        "Gross Income": [12000000, 15000000],
        "Dependents": [0, 1],
        "Region": [1, 2],
        "Net Salary": ["", ""]
    })

    template_buf = io.BytesIO()
    template_df.to_excel(template_buf, index=False)

    st.download_button(
        label="📎 Tải file mẫu",
        data=template_buf.getvalue(),
        file_name="mau_tinh_luong.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.subheader("📤 Upload file tính toán")
    
    uploaded = st.file_uploader("Chọn file Excel", type=['xlsx'])

    if uploaded:
        df_preview = pd.read_excel(uploaded)
        st.info("🔍 Dữ liệu vừa tải lên:")
        st.dataframe(df_preview)

        if st.button("🚀 Bắt đầu tính lương"):
            try:
                res = requests.post(f"{API_URL}/api/net/batch",
                                    files={"file": (uploaded.name, uploaded.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")})
                if res.status_code == 200:
                    result = res.json()
                    df_result = pd.DataFrame(result['data'])
                    st.success("✅ Đã tính lương thành công!")
                    st.dataframe(df_result)

                    # Tải về kết quả
                    output = io.BytesIO()
                    df_result.to_excel(output, index=False)
                    st.download_button("📥 Tải kết quả", output.getvalue(), "salary_result.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                else:
                    st.error(f"❌ Lỗi server: {res.status_code}")
            except Exception as e:
                st.error(f"⚠️ Lỗi khi gửi file: {str(e)}")

st.markdown("---")
st.caption("jaydenhoang5291 😎")
