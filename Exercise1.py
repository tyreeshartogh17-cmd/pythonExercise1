# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input (" Enter your name:")
# TODO: Ask the user for their age and store it in a variable
age = int(input("Please enter your age: "))
# TODO: Print a greeting using the name and age variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}! You are {age} years old.")
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("Enter the length of the rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("Enter the width of the rectangle: "))
# TODO: Calculate the area of the rectangle
def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle given its length and width."""
    return length * width
length = 10.5
width = 5.0

area = calculate_rectangle_area("length, width")

print(f"The area of the rectangle is: {area}")
# TODO: Print the result

#------------------------------------------------------------------------------------
# Question 3: Working with Floats
# TODO:Ask the user for a temperature in Celsius and store it as a float
celsius = float(input("Enter temperature in Celsius: "))
# TODO:Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
# Define the temperature in Celsius
celsius = 25
# Apply the conversion formula
fahrenheit = (celsius * 9/5) + 32
# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
# TODO: Print the result rounded to two decimal places
result = 3.14159265
# TODO: Print the result rounded to two decimal places python code
print(f"{result:.2f}")  # Output: 3.14
# Handles trailing zeros correctly
total = 12.5
print(f"{total:.2f}")   # Output: 12.50
