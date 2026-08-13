from models.employee import Employee
from exceptions.employee_not_found_error import EmployeeNotFoundError
import logging

class EmployeeManager:
    logger = logging.getLogger(__name__)
    def __init__(self, storage):
        self.storage = storage
        self._employees = {}
        self._next_employee_id = 101

    def _generate_employee_id(self):
        employee_id = self._next_employee_id
        self._next_employee_id += 1
        return employee_id

    def get_all_employees(self):
        return list(self._employees.values()) 

    def _get_employee_or_raise(self, employee_id):
        employee = self.search_employee(employee_id)
        if employee is None:
            self.logger.warning(
                "Employee %s was not found",
                employee_id
            )
            raise EmployeeNotFoundError(employee_id)
        return employee   

    def update_employee_department(self,employee_id,department):
        employee = self._get_employee_or_raise(employee_id)
        employee.update_department(department)
        self.storage.save(
            self.get_all_employees()
        )
        self.logger.info(
            "Employee %s department updated to %s",
            employee_id,
            department
        )

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

        self._employees[employee_id] = employee

        self.storage.save(
            self.get_all_employees()
        )
        self.logger.info(
            "Employee %s added successfully",
            employee_id
        )
        return employee

    def search_employee(self, employee_id):      
        return self._employees.get(employee_id)

    def load_employees(self):
        employee_data = self.storage.load()
        for data in employee_data:
            employee = Employee.from_dict(data)
            self._employees[employee.employee_id] = employee
        if self._employees:
            self._next_employee_id = (
                max(self._employees.keys()) + 1
            )