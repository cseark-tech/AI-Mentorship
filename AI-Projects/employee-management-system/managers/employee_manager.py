from models.employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = {}
        self.next_employee_id = 101

    def _generate_employee_id(self):
        employee_id = self.next_employee_id
        self.next_employee_id += 1
        return employee_id

    def add_employee(
            self,
            name,
            dob,
            joining_date,
            department,
            salary
    ):
        employee_id = self._generate_employee_id()

        employee = Employee(
            employee_id,
            name,
            dob,
            joining_date,
            department,
            salary
        )

        self.employees[employee_id] = employee
        return employee

    def search_employee(self, employee_id):
        return self.employees.get(employee_id)