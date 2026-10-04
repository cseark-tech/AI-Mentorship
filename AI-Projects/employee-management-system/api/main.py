from fastapi import FastAPI
from managers.employee_manager import EmployeeManager
from storage.json_storage import JsonStorage
from api.schemas import EmployeeResponse,EmployeeCreateRequest

app = FastAPI()
storage = JsonStorage("data/employees.json")
manager = EmployeeManager(storage)

manager.load_employees()

@app.get("/")
def home():
    return {"message": "Employee Management API is running"}

@app.get("/employees",
          response_model=list[EmployeeResponse])
def get_employees():
    employees = manager.get_all_employees()
    return [
        employee.to_dict()
        for employee in employees
    ]

@app.post("/employees",
          response_model=EmployeeCreateRequest,
          status_code=201)
def create_employee(request: EmployeeCreateRequest):
    employee = manager.add_employee(
        request.name,
        request.dob,
        request.joining_date,
        request.department,
        request.salary
    )
    return employee.to_dict()