from fastapi import FastAPI,HTTPException
from managers.employee_manager import EmployeeManager
from storage.json_storage import JsonStorage
from api.schemas import EmployeeResponse,EmployeeCreateRequest,EmployeeUpdateRequest
from exceptions.employee_not_found_error import EmployeeNotFoundError

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

@app.get("/employees/{employee_id}",
         response_model=EmployeeResponse)
def get_employee(employee_id: int):
    try:
        employee = manager.get_employee(employee_id)
        return employee.to_dict()

    except EmployeeNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@app.patch(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    request: EmployeeUpdateRequest
):
    try:
        employee = manager.update_employee(
            employee_id,
            request.department,
            request.salary
        )

        return employee.to_dict()

    except EmployeeNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@app.delete("/employees/{employee_id}",
            status_code=204)
def delete_employee(employee_id: int):
    try:
        manager.delete_employee(employee_id)
    except EmployeeNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )