from datetime import date
from models.employee import Employee

employee = Employee(
    employee_id=101,
    name="Arun",
    dob=date(1990, 6, 15),
    joining_date=date(2020, 1, 10),
    department="Engineering",
    salary=80000
)

employee.display_details()

print("Age:", employee.calculate_age())
print("Experience: ", employee.calculate_experience())
employee.update_salary(100000)
print("Updated salary:",employee.salary)