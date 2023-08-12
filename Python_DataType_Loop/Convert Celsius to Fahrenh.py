# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking input from the user in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Printing the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")