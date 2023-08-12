# Start the algorithm
print("Welcome to the Rectangle Analyzer!")
print("This program calculates the area and perimeter of a rectangle.")

# Accept the length and width of a rectangle from the user
length = float(input("Enter the length of the rectangle (in units): "))
width = float(input("Enter the width of the rectangle (in units): "))

# Calculate the area of the rectangle
area = length * width

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + width)

# Print the calculated area and perimeter
print("The area of the rectangle is:", area, "square units.")
print("The perimeter of the rectangle is:", perimeter, "units.")

# Compare the area and perimeter and print the corresponding message
if area > perimeter:
    print("The rectangle has a larger area than perimeter.")
elif area == perimeter:
    print("The rectangle has equal area and perimeter.")
else:
    print("The rectangle has a larger perimeter than area.")

# End the algorithm
print("Thank you for using the Rectangle Analyzer!")