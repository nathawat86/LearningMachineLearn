# Accept name and age from the user
name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))

# Check if the user is a valid voter
if age >= 18:
    print("Hello Dear,", name + "! You are eligible to vote.")
else:
    print("Hello Dear,", name + "! You are not eligible to vote yet. Wait for ",(18-age), 'more years to vote.')