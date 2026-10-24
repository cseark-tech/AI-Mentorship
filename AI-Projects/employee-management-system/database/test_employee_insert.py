from datetime import date

from database.connection import SessionLocal
from database.models import EmployeeModel


session = SessionLocal()

try:
    employee = EmployeeModel(
        employee_id=102,
        name="Jack",
        dob=date(1990, 5, 15),
        joining_date=date(2017, 6, 1),
        department="CSE",
        salary=75100
    )

    session.add(employee)

    session.commit()

    print("Employee inserted successfully!")

except Exception as error:
    session.rollback()
    print("Insert failed:")
    print(error)

finally:
    session.close()