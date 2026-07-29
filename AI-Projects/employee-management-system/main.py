from datetime import date
from managers.employee_manager import EmployeeManager
from storage.storage import Storage

storage = Storage()
manager = EmployeeManager(storage)
storage.save(manager.employees)

employee1 = manager.add_employee(
    "Arun",
    date(1990, 6, 15),
    date(2020, 1, 10),
    "Engineering",
    80000
)

employee2 = manager.add_employee(
    "John",
    date(1995, 7, 20),
    date(2023, 2, 1),
    "QA",
    45000
)

print(print(f"Employee ID: {employee1.employee_id}"))
print(print(f"Employee ID: {employee2.employee_id}"))

employee = manager.search_employee(102)

if employee:
    employee.display_details()