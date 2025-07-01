"""
🔰 Python Basics: 12 Essential Beginner Problems
This script solves beginner-level Python problems in a clean and well-commented way.
"""

# 1. ✅ Swap two variables without using a third variable
print(" 1. Swap Two Variables Without Third Variable")
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}\n")

# 2. ✅ Find the area of a circle with a given radius
print(" 2. Area of a Circle")
import math
radius = 5
area = math.pi * radius**2
print(f"Area of the circle with radius {radius} is: {area:.2f}\n")

# 3. ✅ Convert Celsius to Fahrenheit
print(" 3. Celsius to Fahrenheit")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit:.2f}\n")

# 4. ✅ Calculate the simple interest
print(" 4. Simple Interest")
P = 1000  # Principal
R = 5     # Annual rate
T = 3     # Time in years
SI = (P * R * T) / 100
print(f"Simple Interest is: {SI:.2f}\n")

# 5. ✅ Get ASCII value of a character
print(" 5. ASCII Value of a Character")
char = 'A'
ascii_val = ord(char)
print(f"The ASCII value of '{char}' is {ascii_val}\n")

# 6. ✅ Take user input and display data type
print(" 6. User Input and Data Type")
user_input = input("Enter something: ")
print(f"You entered: {user_input}")
print("Data type:", type(user_input), "\n")

# 7. ✅ Add two float numbers
print(" 7. Add Two Float Numbers")
num1 = 3.5
num2 = 6.7
result = num1 + num2
print(f"Sum of {num1} and {num2} is {result}\n")

# 8. ✅ Calculate the square and cube of a number
print(" 8. Square and Cube")
number = 4
square = number ** 2
cube = number ** 3
print(f"Square of {number} is {square}")
print(f"Cube of {number} is {cube}\n")

# 9. ✅ Find the perimeter of a rectangle
print(" 9. Perimeter of a Rectangle")
length = 8
width = 6
perimeter = 2 * (length + width)
print(f"Perimeter of rectangle (L={length}, W={width}) is {perimeter}\n")

# 10. ✅ Calculate the compound interest
print(" 10. Compound Interest")
P = 2000
R = 4
T = 2
CI = P * (1 + R / 100) ** T - P
print(f"Compound Interest is {CI:.2f}\n")

# 11. ✅ Convert seconds into hours, minutes, and seconds
print(" 11. Convert Seconds into H:M:S")
total_seconds = 7384
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds is {hours}h {minutes}m {seconds}s\n")

# 12. ✅ Print first and last characters of a string
print(" 12. First and Last Character of a String")
string_input = input("Enter a string: ")
if len(string_input) > 0:
    print(f"First character: {string_input[0]}")
    print(f"Last character: {string_input[-1]}")
else:
    print("You entered an empty string.")
