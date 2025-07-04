"""
🧠 Python Functions Practice - Beginner to Intermediate
A collection of functions to perform various mathematical and string operations.
"""

# 1. ✅ Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. ✅ Calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 3. ✅ Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. ✅ Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# 5. ✅ Calculator using functions
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# 6. ✅ Recursive Fibonacci function
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 7. ✅ Find maximum of 3 numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 8. ✅ Find length of a string
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# 9. ✅ Sum of a list
def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# 10. ✅ Check Armstrong number
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    return total == n

# 11. ✅ Reverse a string
def reverse_string(s):
    return s[::-1]

# === Example Usage ===
if __name__ == "__main__":
    print("Is 7 prime?", is_prime(7))
    print("Factorial of 5:", factorial(5))
    print("Is 'radar' a palindrome?", is_palindrome("radar"))
    print("Vowel count in 'Hello World':", count_vowels("Hello World"))
    print("Calculator (10 * 5):", calculator(10, 5, "multiply"))
    print("Fibonacci (5th term):", fibonacci_recursive(5))
    print("Max of (10, 22, 13):", max_of_three(10, 22, 13))
    print("Length of 'Python':", string_length("Python"))
    print("Sum of list [1, 2, 3, 4]:", list_sum([1, 2, 3, 4]))
    print("Is 153 Armstrong?", is_armstrong(153))
    print("Reverse of 'hello':", reverse_string("hello"))
    

