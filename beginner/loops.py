"""
🔁 Python Loop Practice Problems
This script contains beginner-level Python questions focusing on loops,
patterns, number operations, and mathematical logic.
"""

# 1. ✅ Print numbers from 1 to 100
print("🔹 1. Numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# 2. ✅ Multiplication table of a number
print("🔹 2. Multiplication Table")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# 3. ✅ Sum of first N natural numbers
print("🔹 3. Sum of First N Natural Numbers")
N = int(input("Enter N: "))
sum_n = sum(range(1, N + 1))
print(f"Sum of first {N} natural numbers is {sum_n}\n")

# 4. ✅ Display Fibonacci series up to N terms
print("🔹 4. Fibonacci Series")
n_terms = int(input("How many Fibonacci terms? "))
a, b = 0, 1
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 5. ✅ Prime numbers between two numbers
print("🔹 5. Prime Numbers in Range")
start = int(input("Start number: "))
end = int(input("End number: "))
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if num > 1:
        for div in range(2, int(num**0.5) + 1):
            if num % div == 0:
                break
        else:
            print(num, end=" ")
print("\n")

# 6. ✅ Reverse of a number
print("🔹 6. Reverse a Number")
num = int(input("Enter a number to reverse: "))
reverse = 0
original = num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(f"Reverse of {original} is {reverse}\n")

# 7. ✅ Count digits in a number
print("🔹 7. Count Digits in a Number")
num = int(input("Enter a number: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print(f"Total digits in {num} = {count}\n")

# 8. ✅ Factorial of a number
print("🔹 8. Factorial of a Number")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}\n")

# 9. ✅ Sum of even numbers between 1 and N
print("🔹 9. Sum of Even Numbers from 1 to N")
n = int(input("Enter a value for N: "))
even_sum = sum(i for i in range(2, n + 1, 2))
print(f"Sum of even numbers from 1 to {n} is {even_sum}\n")

# 10. ✅ Triangle pattern with stars
print("🔹 10. Triangle of Stars")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
print()

# 11. ✅ Multiplication tables from 1 to 10
print("🔹 11. Multiplication Tables from 1 to 10")
for i in range(1, 11):
    print(f"--- Table of {i} ---")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

# 12. ✅ Sum of digits in a number
print("🔹 12. Sum of Digits in a Number")
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print(f"Sum of digits in {num} is {sum_digits}")
