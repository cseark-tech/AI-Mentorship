from sqlalchemy import Column, Integer, String, Float, Date
from database.connection import Base
from models.employee import Employee


class EmployeeModel(Base):

    __tablename__ = "employees"

    employee_id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    dob = Column(
        Date,
        nullable=False
    )

    joining_date = Column(
        Date,
        nullable=False
    )

    department = Column(
        String(100),
        nullable=False
    )

    salary = Column(
        Float,
        nullable=False
    )

    @classmethod
    def from_domain(cls, employee):
        return cls(
            employee_id=employee.employee_id,
            name=employee.name,
            dob=employee.dob,
            joining_date=employee.joining_date,
            department=employee.department,
            salary=employee.salary
        )

    def to_domain(self):
        return Employee(
            employee_id=self.employee_id,
            name=self.name,
            dob=self.dob,
            joining_date=self.joining_date,
            department=self.department,
            salary=self.salary
        )