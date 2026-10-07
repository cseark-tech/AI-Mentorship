from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeCreateRequest(BaseModel):
    name: str
    dob: date
    joining_date: date
    department: str
    salary: float

class EmployeeResponse(BaseModel):
    employee_id: int
    name: str
    dob: date
    joining_date: date
    department: str
    salary: float

class EmployeeUpdateRequest(BaseModel):
    department: Optional[str] = None
    salary: Optional[float] = None

