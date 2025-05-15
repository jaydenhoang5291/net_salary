# 💼 Net Salary Calculator

This project delivers a simple and user-friendly web application that helps users calculate **Net Salary** from **Gross Salary** by automatically deducting insurance and personal income tax. It also supports **batch salary calculations via Excel file upload**.

## 🏗️ System Architecture

The system follows a basic **client-server architecture**, where:

- Users interact with a simple and intuitive web interface built with **Streamlit (frontend)**.
- User input is sent to a **FastAPI (backend)** server, which handles business logic and salary calculation.
- Both frontend and backend are containerized using **Docker**, and orchestrated using **Docker Compose**.
- The system is continuously tested and deployed using **CI/CD pipelines (GitHub Actions)**, with deployment targets hosted on **Render**.
- The project adopts a **monorepo structure** to simplify development, versioning, and deployment.

```
            +------------------+
            |    User Input    |
            +--------+---------+
                     |
                     v
     +---------------+----------------+
     |         Frontend (Streamlit)   |
     |  - Dockerized                  |
     |  - Sends requests to backend   |
     +---------------+----------------+
                     |
                     v
     +---------------+----------------+
     |         Backend (FastAPI)      |
     |  - Dockerized                  |
     |  - Exposes API for salary calc |
     +---------------+----------------+
                     |
                     v
     +---------------+----------------+
     |         Cloud Deployment       |
     |    (Docker Compose on Render)  |
     +--------------------------------+
```

## 📁 Project Structure

```
.github/
    └── workflows/              # CI workflow for GitHub Actions
        └── github-actions.yaml # Runs tests and prepares for deployment
backend/                        
    ├── api/                 
        └── endpoints/          # API route definitions
    ├── models/                 # Pydantic schemas for request/response
    ├── services/               # Business logic (net salary computation)
    ├── Dockerfile              # Backend Docker configuration
    ├── main.py                 # FastAPI application entry point
    └── requirements.txt        # Backend Python dependencies
frontend/
    ├── app.py                  # Main UI application
    ├── Dockerfile              # Frontend Docker configuration
    └── requirements.txt        # Frontend Python dependencies
test/
    ├── data/                   # Sample Excel files for batch testing
    ├── conftest.py             # Pytest configuration
    ├── test_routes_net_salary.py      # Tests for API endpoints
    └── test_service_salary_logic.py   # Tests for salary calculation logic
docker-compose.yaml                    # Docker Compose to orchestrate backend & frontend
README.md                              # Project documentation
```

## 🚀 Deployment Guide

### 🖥️ Local Development Setup

#### 1. Clone the repository:

```
git clone https://github.com/jaydenhoang5291/net_salary.git
cd net_salary
```
#### 2. Create and use virtual environment
```
python3 -m venv venv        # Create environment
source venv/bin/activate    # Activate enviroment for Unbuntu
venv\Scripts\Activate      # Activate enviroment for Windows
```
#### 3. Install dependencies
```
cd backend
pip install -r requirements.txt
```
```
cd frontend
pip install -r requirements.txt
```
#### 4. Run Backend
```
uvicorn main:application
```
#### 5. Run Frontend
```
streamlit run app.py
```

### 🐳 Docker Compose
```
cd net_salary
docker compose up -d
```
- Access this link ```http://localhost:8501``` (Frontend (Streamlit UI))
