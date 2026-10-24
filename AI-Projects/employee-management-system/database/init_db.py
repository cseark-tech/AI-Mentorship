from database.connection import engine, Base
from database.models import EmployeeModel

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")