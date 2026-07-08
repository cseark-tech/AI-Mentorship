import json

employees = []
choice: str = 'y'
employee_id: int = 1000


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
    global employee_id 
    employee_id += 1
    employee["id"] = employee_id
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




