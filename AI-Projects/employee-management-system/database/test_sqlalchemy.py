from database.connection import engine

try:
    with engine.connect() as connection:
        print("SQLAlchemy connection successful!")

except Exception as error:
    print("Database connection failed:")
    print(error)