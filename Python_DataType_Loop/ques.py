# Take three integer/float inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check if all three numbers are equal
if num1 == num2 and num2 == num3:
    print("All three numbers are equal")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Any two numbers are equal")
else:
    print("None of the numbers are equal")