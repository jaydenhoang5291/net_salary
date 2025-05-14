from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import payroll_api

import uvicorn

application = FastAPI(
    title="Net Salary Service",
    description="Service to estimate net salary from gross income",
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

application.include_router(payroll_api.router)

if __name__ == "__main__":
    uvicorn.run("app.main:application", host="0.0.0.0", port=8000, reload=True)

#khởi tạo fast api app