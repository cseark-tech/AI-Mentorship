import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="employee_management",
    user="postgres",
    password="arunsql26"
)

print("PostgreSQL connection successful!")

connection.close()