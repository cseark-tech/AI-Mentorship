import unittest
from datetime import date

from models.employee import Employee
class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):

        employee = Employee(
                employee_id=101,
                name="Arun",
                dob=date(1990, 6, 15),
                joining_date=date(2020, 1, 10),
                department="Engineering",
                salary=80000
            )

        self.assertEqual(employee.employee_id, 101)
        self.assertEqual(employee.name, "Arun")
        self.assertEqual(employee.salary, 80000)
        self.assertEqual(employee.department, "Engineering")
        self.assertEqual(employee.salary, 80000)