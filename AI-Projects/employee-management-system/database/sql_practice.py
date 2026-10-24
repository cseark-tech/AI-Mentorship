import sqlite3

connection = sqlite3.connect("database/employees.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL NOT NULL
    )
""")

# cursor.execute("""
#     INSERT INTO employees
#     (employee_id, name, department, salary)
#     VALUES (?, ?, ?, ?)
# """, (101, "Arun", "IT", 70000))

cursor.execute("""
    INSERT INTO employees
    (employee_id, name, department, salary)
    VALUES (?, ?, ?, ?)
""", (103, "Ravi", "HR", 60000))

cursor.execute("""
    UPDATE employees SET salary=52000 where employee_id=102
""")

cursor.execute("""
    DELETE FROM employees WHERE employee_id=101
""")

cursor.execute("""
    SELECT employee_id, name, department, salary
    FROM employees
""")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

connection.commit()

connection.close()