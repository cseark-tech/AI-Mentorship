print("Two number Operation")
def error_message():
     print("Enter a valid number")
     exit()

try:
    num1 = float(input("Enter first number: "))
except ValueError:
    error_message()
try:
    num2 = float(input("Enter second number: "))
except ValueError:
    error_message()

operator = input("Choose any operator +, -, *, /: ")
result = None
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2   
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print(f"Cannot divide by zero")
    else:
        result = num1 / num2
else:
    print(f"Invalid operator")

if result is not None:
    print(f"Result = {result}")

