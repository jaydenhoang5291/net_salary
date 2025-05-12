from fastapi import APIRouter, UploadFile, File, HTTPException
from models.schemas import NetSalaryRequest, NetSalaryResponse, SalaryBatchResponse, SalaryRecord
from services.calculator import NetSalaryCalculator
import pandas as pd
from io import BytesIO

router = APIRouter(prefix="/api/net", tags=["Payroll"])

@router.post("/single", response_model=NetSalaryResponse)
def compute_single_salary(payload: NetSalaryRequest):
    result = NetSalaryCalculator.calculate(payload.gross, payload.dependents)
    return result

@router.post("/batch", response_model=SalaryBatchResponse)
async def compute_bulk_salary(file: UploadFile = File(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        content = await file.read()
        df = pd.read_excel(BytesIO(content))

        required = ["Employee ID", "Name", "Gross Income", "Dependents"]
        if not all(col in df.columns for col in required):
            raise HTTPException(status_code=400, detail="Missing required columns")

        entries = []
        for _, row in df.iterrows():
            result = NetSalaryCalculator.calculate(
                gross=row["Gross Income"],
                dependents=row["Dependents"]
            )
            entries.append(SalaryRecord(
                employee_id=row["Employee ID"],
                name=row["Name"],
                gross_income=row["Gross Income"],
                dependents=row["Dependents"],
                net_income=result.net_salary
            ))

        return SalaryBatchResponse(data=entries)
    except Exception as e:
        print("📛 Lỗi khi xử lý Excel:", e)
        raise HTTPException(status_code=500, detail=f"Failed to process file: {e}")

#Xử lý route