from datetime import date
from managers.employee_manager import EmployeeManager
from storage.json_storage import JsonStorage

storage = JsonStorage()
manager = EmployeeManager(storage)


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

employee3 = manager.add_employee(
    "Jack",
    date(1995, 10, 20),
    date(2025, 2, 1),
    "QA",
    55000
)

employee = manager.search_employee(102)

if employee:
    employee.display_details()