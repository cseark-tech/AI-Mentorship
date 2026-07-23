import json

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
            raise ValueError("Employee name cannot be empty")
        
    def _validate_salary(self, salary):
        if salary < 0:
            raise ValueError("salary cannot be negative")
        
    def update_salary(self, new_salary):
        self._validate_salary(new_salary)
        self.salary = new_salary
        print("Salary updated successfully.")
    
    def display_details(self):
        print("Employee ID: ", self.employee_id)
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Salary: ", self.salary)

employee = Employee(
    101,
    "Arun",
    "15-06-1990",
    "10-01-2020",
    "Engineering",
    80000
)
employee.display_details()
employee.update_salary(90000)
employee.display_details()
employee.update_salary(-500)

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




