def mod_two_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if b != 0:
        result = a % b
        print(f"The result of {a} % {b} is: {result}")
    else:
        print("Error: Modulus by zero is not allowed.")

# Call the function
mod_two_numbers()
