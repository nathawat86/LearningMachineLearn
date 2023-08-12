# Function to calculate the sum of a list of numbers
def get_sum_fun1(num_list):
    return sum(num_list)

# Function to calculate the average of a list of numbers
def get_average_fun2(num_list):
    return sum(num_list) / len(num_list)

# Function to take user input, sort the numbers, and calculate sum and average
def main_prog_func():
    num_list = []
    for i in range(3):  # Loop to take input for 3 numbers
        num = float(input(f"Enter number {i + 1}: "))
        num_list.append(num)

    # Sort the numbers in ascending order
    num_list.sort()

    # Calculate and print the sorted numbers, sum, and average
    print(f"Sorted numbers: {num_list}")
    print(f"Sum of the numbers: {get_sum_fun1(num_list)}")
    print(f"Average of the numbers: {get_average_fun2(num_list)}")

if __name__ == "__main__":
    main_prog_func()  # Call the main function three times
    main_prog_func()
    main_prog_func()
