from pydantic import BaseModel
from datetime import date

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

