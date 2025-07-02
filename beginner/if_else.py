"""
🔰 Beginner Python - Conditional Statements Practice
A collection of simple if-else problems with practical, well-written Python solutions.
"""

# 1. Check if a number is even or odd
print("🔹 1. Even or Odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.\n")
else:
    print(f"{num} is odd.\n")

# 2. Find the largest of three numbers
print("🔹 2. Largest of Three Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"The largest number is: {largest}\n")

# 3. Check if a year is a leap year
print("🔹 3. Leap Year Check")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.\n")
else:
    print(f"{year} is not a leap year.\n")

# 4. Assign grade based on percentage
print("🔹 4. Grade Based on Percentage")
marks = float(input("Enter your percentage: "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"
print(f"Your grade is: {grade}\n")

# 5. Check if a number is positive, negative, or zero
print("🔹 5. Number Sign Check")
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.\n")
elif number < 0:
    print("The number is negative.\n")
else:
    print("The number is zero.\n")

# 6. Check whether a character is a vowel or consonant
print("🔹 6. Vowel or Consonant")
char = input("Enter a single alphabet character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.\n")
elif char.isalpha():
    print(f"{char} is a consonant.\n")
else:
    print("Invalid input. Please enter an alphabet.\n")

# 7. Check if a number is divisible by 5 and 11
print("🔹 7. Divisibility by 5 and 11")
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.\n")
else:
    print(f"{num} is not divisible by both 5 and 11.\n")

# 8. Check if a number is prime
print("🔹 8. Prime Number Check")
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.\n")
            break
    else:
        print(f"{num} is a prime number.\n")
else:
    print(f"{num} is not a prime number.\n")

# 9. Check if a character is uppercase or lowercase
print("🔹 9. Uppercase or Lowercase")
char = input("Enter a single alphabet character: ")
if char.isupper():
    print(f"{char} is uppercase.\n")
elif char.islower():
    print(f"{char} is lowercase.\n")
else:
    print("Invalid input. Please enter a valid alphabet.\n")

# 10. Calculate electricity bill with conditions
print("🔹 10. Electricity Bill Calculator")
units = float(input("Enter electricity units consumed: "))
if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
bill += bill * 0.20  # Adding 20% surcharge
print(f"Total electricity bill is: Rs. {bill:.2f}\n")

# 11. Check whether a person is eligible to vote
print("🔹 11. Voter Eligibility Check")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.\n")
else:
    print("You are not eligible to vote yet.\n")

# 12. Find roots of a quadratic equation
print("🔹 12. Roots of Quadratic Equation")
import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + discriminant) / (2*a)
root2 = (-b - discriminant) / (2*a)

print(f"The roots of the equation are: {root1} and {root2}\n")
