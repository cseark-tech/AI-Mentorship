from sqlalchemy import select

from database.connection import SessionLocal
from database.models import EmployeeModel


session = SessionLocal()

try:

    statement = select(EmployeeModel)

    employees = session.scalars(statement).all()

    for employee in employees:
        print(
            employee.employee_id,
            employee.department,
            employee.dob
        )

finally:
    session.close()