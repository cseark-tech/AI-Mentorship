employees = []
choice: str = 'y'

def error_message():
    print("Please Enter valid numbers")
    exit()

def add_employee():
    employee = {
    "name": "",
    "age": "",
    "experience": "",
    "salary": ""
    }
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
    print("Employee added successfully.")    

def view_employees():   
    if not employees:
        print("No employees found")
        return
    employee_number = 1
    for employee in employees:
        print("------------------")
        print(f"Employee {employee_number}")
        print("-------------------")
        print(f"Name: {employee['name']}")
        print(f"Age: {employee['age']}")
        print(f"Experience: {employee['experience']}")
        print(f"Salary: {employee['salary']}")
        print()
        employee_number +=1


while choice == "y":
    add_employee()
    choice = input("Do you want to add another employee? (y/n): ").lower()    
view_employees()




