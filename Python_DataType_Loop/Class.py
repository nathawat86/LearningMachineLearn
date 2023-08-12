# Number of rows for the pattern
num_rows = int(input("Enter the number of rows: "))

# Outer loop to iterate through each row
for i in range(num_rows):
    # Inner loop to print stars for each row
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row

print("\n Let's try to print pyramid")

for i in range(num_rows):
    # Inner loop to print spaces before the stars
    for j in range(num_rows - i - 1):
        print(" ", end="")
    
    # Inner loop to print stars for each row
    for k in range(2 * i + 1):
        print("*", end="")
    
    print()  # Move to the next line after each row