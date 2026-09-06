import unittest
from datetime import date
from tempfile import NamedTemporaryFile

from managers.employee_manager import EmployeeManager
from storage.json_storage import JsonStorage

class TestEmployeePersistence(unittest.TestCase):

    def test_employee_can_be_saved_and_loaded(self):

        with NamedTemporaryFile(
            mode="w",
            delete=False
        ) as temp_file:

            file_path = temp_file.name
        storage = JsonStorage(file_path)
        manager = EmployeeManager(storage)
        employee = manager.add_employee(
            "Arun",
            date(1990, 6, 15),
            date(2020, 1, 10),
            "Engineering",
            80000
        )
        print("Created employee ID:", employee.employee_id)

        new_storage = JsonStorage(file_path)
        new_manager = EmployeeManager(new_storage)
        new_manager.load_employees()
        print("Loaded employees:", new_manager.get_all_employees())
        loaded_employee = new_manager.search_employee(101)
        self.assertIsNotNone(loaded_employee)
        self.assertEqual(
            loaded_employee.name,
            "Arun"
        )
        self.assertEqual(
        loaded_employee.department,
        "Engineering"
        )
        self.assertEqual(
        loaded_employee.salary,
        80000
        )