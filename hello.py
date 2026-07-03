name = input("Enter your name")
experience = int(input("Enter your experience"))

print(f"Hello {name}")
print(f"You have {experience} of total experience")

if(experience > 10):
    print("You are a senior software engineer")
else:
    print("You are a software engineer")