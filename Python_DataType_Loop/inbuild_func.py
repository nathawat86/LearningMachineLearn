# Lambda function for greeting the user
greet_user = lambda name: f"Hello, {name}! Welcome to the number operations program."

# Lambda functions for performing operations
add = lambda x, y, z: x + y + z
multiply = lambda x, y, z: x * y * z
average = lambda x, y, z: (x + y + z) / 3
modulus = lambda x, y, z: (x % y) % z

# Get user input
name = input("Enter your name: ")
print(greet_user(name))

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Perform operations using lambda functions
print(f"Sum of the numbers: {add(num1, num2, num3)}")
print(f"Product of the numbers: {multiply(num1, num2, num3)}")
print(f"Average of the numbers: {average(num1, num2, num3)}")
print(f"Modulus of the numbers: {modulus(num1, num2, num3)}")
