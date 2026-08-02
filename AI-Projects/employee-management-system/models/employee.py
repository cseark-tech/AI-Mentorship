from datetime import date

class Employee:

    def __init__(
            self,
            employee_id,
            name,
            dob,
            joining_date,
            department,
            salary
    ):
        self._validate_name(name)
        self._validate_salary(salary)

        self.employee_id = employee_id
        self.name = name
        self.dob = dob
        self.joining_date = joining_date
        self.department = department
        self.salary = salary

    def _validate_name(self, name):
        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

    def _validate_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

    def update_salary(self, new_salary):
        self._validate_salary(new_salary)
        self.salary = new_salary

    def calculate_experience(self):
        today = date.today()

        years = today.year - self.joining_date.year

        if (
            today.month,
            today.day
        ) < (
            self.joining_date.month,
            self.joining_date.day
        ):
            years -= 1

        return years

    def calculate_age(self):
        today = date.today()

        years = today.year - self.dob.year
        if (
            today.month,
            today.day
        ) < (
            self.dob.month,
            self.dob.day
        ):
            years -= 1

        return years

    def display_details(self):

        print(f"ID         : {self.employee_id}")
        print(f"Name       : {self.name}")
        print(f"DOB        : {self.dob}")
        print(f"Department : {self.department}")
        print(f"Salary     : {self.salary}")

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "dob": self.dob.isoformat(),
            "joining_date": self.joining_date.isoformat(),
            "department": self.department,
            "salary": self.salary
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            employee_id=data["employee_id"],
            name=data["name"],
            dob=date.fromisoformat(data["dob"]),
            joining_date=date.fromisoformat(data["joining_date"]),
            department=data["department"],
            salary=data["salary"]
        )