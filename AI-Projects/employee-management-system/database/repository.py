from database.models import EmployeeModel


class EmployeeRepository:

    def __init__(self, session):
        self.session = session

    def save(self, employee):
        db_employee = EmployeeModel.from_domain(employee)

        self.session.add(db_employee)
        self.session.commit()

        return db_employee.to_domain()

    def get_by_id(self, employee_id):
        db_employee = (
            self.session.query(EmployeeModel)
            .filter(
                EmployeeModel.employee_id == employee_id
            )
            .first()
        )

        if db_employee is None:
            return None

        return db_employee.to_domain()

    def get_all(self):
        db_employees = (
            self.session
            .query(EmployeeModel)
            .all()
        )

        return [
            employee.to_domain()
            for employee in db_employees
        ]

    def get_next_employee_id(self):
        employees = self.get_all()

        if not employees:
            return 101

        return max(
            employee.employee_id
            for employee in employees
        ) + 1

    def update(self, employee):
        db_employee = (
            self.session.query(EmployeeModel)
            .filter(
                EmployeeModel.employee_id == employee.employee_id
            )
            .first()
        )

        if db_employee is None:
            return None

        db_employee.name = employee.name
        db_employee.dob = employee.dob
        db_employee.joining_date = employee.joining_date
        db_employee.department = employee.department
        db_employee.salary = employee.salary

        self.session.commit()

        return db_employee.to_domain()

    def delete(self, employee_id):
        db_employee = (
            self.session.query(EmployeeModel)
            .filter(
                EmployeeModel.employee_id == employee_id
            )
            .first()
        )

        if db_employee is None:
            return None

        self.session.delete(db_employee)
        self.session.commit()

        return db_employee.to_domain()