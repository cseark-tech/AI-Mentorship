from logging_config import configure_logging
from datetime import date
from managers.employee_manager import EmployeeManager
from storage.json_storage import JsonStorage

configure_logging()
storage = JsonStorage()
manager = EmployeeManager(storage)
manager.load_employees()


# employee1 = manager.add_employee(
#     "Arun",
#     date(1990, 6, 15),
#     date(2020, 1, 10),
#     "Engineering",
#     80000
# )

# employee2 = manager.add_employee(
#     "John",
#     date(1995, 7, 20),
#     date(2023, 2, 1),
#     "QA",
#     45000
# )

# employee3 = manager.add_employee(
#     "Jill cleek",
#     date(1995, 10, 20),
#     date(2025, 2, 1),
#     "Manager",
#     550000
# )

manager.update_employee_department(108,"TECH")

employee = manager.search_employee(999)


if employee:
    employee.display_details()

