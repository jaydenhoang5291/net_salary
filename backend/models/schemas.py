from pydantic import BaseModel
from typing import List, Optional

class NetSalaryRequest(BaseModel):
    gross: float
    dependents: int

class NetSalaryResponse(BaseModel):
    gross_salary: float
    net_salary: float
    insurance_fee: float
    tax_due: float

class SalaryRecord(BaseModel):
    employee_id: int
    name: str
    gross_income: float
    dependents: int
    net_income: Optional[float] = None

class SalaryBatchResponse(BaseModel):
    data: List[SalaryRecord]

#định nghĩa dữ liệu