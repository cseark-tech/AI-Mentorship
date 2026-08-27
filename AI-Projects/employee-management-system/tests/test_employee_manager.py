import unittest
from datetime import date
from unittest.mock import Mock

from managers.employee_manager import EmployeeManager
from exceptions.employee_not_found_error import EmployeeNotFoundError


class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.storage = Mock()
        self.manager = EmployeeManager(self.storage)

    def test_add_employee(self):

        employee = self.manager.add_employee(
            "Arun",
            date(1990, 6, 15),
            date(2020, 1, 10),
            "Engineering",
            80000
        )

        self.assertEqual(employee.employee_id, 101)
        self.assertEqual(employee.name, "Arun")
        self.assertEqual(employee.salary, 80000)

    def test_employee_ids_are_generated_sequentially(self):

        employee1 = self.manager.add_employee(
            "Arun",
            date(1990, 6, 15),
            date(2020, 1, 10),
            "Engineering",
            80000
        )

        employee2 = self.manager.add_employee(
            "John",
            date(1995, 7, 20),
            date(2023, 2, 1),
            "QA",
            45000
        )

        self.assertEqual(employee1.employee_id, 101)
        self.assertEqual(employee2.employee_id, 102)

    def test_search_employee(self):

        employee = self.manager.add_employee(
            "Arun",
            date(1990, 6, 15),
            date(2020, 1, 10),
            "Engineering",
            80000
        )

        result = self.manager.search_employee(
            employee.employee_id
        )

        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Arun")

    def test_update_department_employee_not_found(self):

        with self.assertRaises(EmployeeNotFoundError):

            self.manager.update_employee_department(
                999,
                "TECH"
            )

    def test_update_employee_department(self):

        employee = self.manager.add_employee(
            "Arun",
            date(1990, 6, 15),
            date(2020, 1, 10),
            "Engineering",
            80000
        )

        self.manager.update_employee_department(
            employee.employee_id,
            "TECH"
        )

        self.assertEqual(
            employee.department,
            "TECH"
        )