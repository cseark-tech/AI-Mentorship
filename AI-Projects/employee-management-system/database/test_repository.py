from database.connection import SessionLocal
from database.repository import EmployeeRepository


session = SessionLocal()

try:
    repository = EmployeeRepository(session)

    employee = repository.get_by_id(101)

    if employee:
        print("Employee found:")
        print(employee.employee_id)
        print(employee.name)
        print(employee.department)
        print(employee.salary)
    else:
        print("Employee not found.")

    employees = repository.get_all()
    print("\nAll employees:")

    for employee in employees:
        print(
            f"ID: {employee.employee_id}, "
            f"Name: {employee.name}, "
            f"Department: {employee.department}, "
            f"Salary: {employee.salary}"
        )
    deleteEmp = repository.delete(102)

finally:
    session.close()