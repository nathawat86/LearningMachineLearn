# Accept the gender from the user
gender = input("Enter your gender (M for Male, F for Female): ")

# Check the gender and print the respective greeting messagem
if gender == 'M' or gender == 'm':
    print("Very Good Morning Sir!")
elif gender == 'F' or gender == 'f':
    print("Very Good Morning Ma'am!")
else:
    print("Invalid gender entered.")