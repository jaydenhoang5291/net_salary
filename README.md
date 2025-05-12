để chạy frontend

cd frontend

streamlit run app.py


để chạy backend

cd ngu
PYTHONPATH=backend uvicorn backend.main:application --reload
