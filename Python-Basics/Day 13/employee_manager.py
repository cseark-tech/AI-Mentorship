import json

class Employee:
    def __init__(
            self,            
            employee_id,
            name,
            salary
            ):
        self._validate_salary(salary),
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def _validate_salary(self, salary):
        if salary < 0:
            raise ValueError("salary cannot be negative")

employee = Employee(
    101,
    "Arun",
    80000
)
employee = Employee(
    102,
    "jack",
    -80000
)
print(employee.salary)
print(employee.name)

class EmployeeManager:

    def __init__(self):
        self.employees = []

    def view_employees(self):
        print(self.employees)

manager = EmployeeManager()
manager.view_employees()

employees = []
choice: str = 'y'

def get_next_employee_id():
    if not employees:
       return 1000
    else:
        employee_id = employees[0]['id']
        for employee in employees:
            if employee['id'] > employee_id:
               employee_id = employee["id"]
        return employee_id       

def error_message():
    print("Please Enter valid numbers")
    exit()

def load_employees():
    global employees
    with open("../../data/employees.json", "r") as file:
        employees = json.load(file)

def save_employees():
    with open("../../data/employees.json", "w") as file:
        json.dump(employees, file, indent=4)

def add_employee():
    employee = {
    "name": "",
    "age": "",
    "experience": "",
    "salary": "",
    "id": 0
    }
    # global employee_id 
    next_id = get_next_employee_id() + 1
    employee["id"] = next_id
    employee["name"] = input("Please enter Employee Name: ")
    try: 
        employee["age"] = int(input("Please enter Employee Age: "))
    except ValueError: 
        error_message()
    try: 
        employee["experience"] = int(input("Please enter Employee Experience: "))
    except ValueError: 
        error_message()
    try: 
        employee["salary"] = float(input("Please enter Employee Salary: "))
    except ValueError: 
        error_message()
    employees.append(employee)
    save_employees()
    print("Employee added successfully.")    

def view_employees():   
    if not employees:
        print("No employees found")
        return
    employee_number = 1
    for employee in employees:       
        display_employeeList(employee, employee_number)
        employee_number +=1

def search_employee():
    try:
        search_id = int(input("Enter Employee ID to search from employees list: "))
    except ValueError:
        error_message()
    employee_number = 1
    found = False
    for employee in employees:
        if employee['id'] == search_id:
            found = True
            display_employeeList(employee, employee_number)
            employee_number +=1
            break
    if not found:
        print("No employee found")

def display_employeeList(emp, empnumber):
    print("------------------")
    print(f"Employee {empnumber}")
    print("-------------------")
    print(f"ID: {emp['id']}")
    print(f"Name: {emp['name']}")
    print(f"Age: {emp['age']}")
    print(f"Experience: {emp['experience']}")
    print(f"Salary: {emp['salary']}")
    print()

load_employees()
while choice == "y":
    add_employee()
    choice = input("Do you want to add another employee? (y/n): ").lower()    
view_employees()
search_employee()




