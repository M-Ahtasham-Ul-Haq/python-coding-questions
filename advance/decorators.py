"""
📘 Python Decorators Practice
This script includes 10 custom decorators for logging, validation, debugging, and advanced control.
Each decorator is explained and used with sample functions for clarity.
"""

import time
import functools

# 1. ✅ Decorator to log function execution time
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

# 2. ✅ Decorator to validate if argument is positive
def positive_only(func):
    @functools.wraps(func)
    def wrapper(n):
        if n <= 0:
            return "❌ Error: Input must be positive!"
        return func(n)
    return wrapper

# 3. ✅ Decorator that repeats function N times
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# 4. ✅ Memoization decorator (cache results)
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

# 5. ✅ Decorator for debugging function name and arguments
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🔍 Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# 6. ✅ Use multiple decorators on one function
@log_execution_time
@debug
def multiply(a, b):
    time.sleep(0.1)
    return a * b

# 7. ✅ Create decorator for access control (admin/user)
def access_control(role_required):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user_role):
            if user_role != role_required:
                return f"🚫 Access denied: {role_required} only!"
            return func(user_role)
        return wrapper
    return decorator

# 8. ✅ Time delay decorator
def delay(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"⏳ Waiting {seconds} seconds...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 9. ✅ Decorator to skip execution if condition not met
def skip_if_false(condition):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not condition:
                print("⚠️ Skipped due to condition=False")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 10. ✅ Decorator that returns function output in uppercase
def to_uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

# === Example Usage ===
if __name__ == "__main__":

    @positive_only
    def square_root(n):
        return n ** 0.5

    @repeat(3)
    def greet():
        print("Hello!")

    @memoize
    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    @access_control("admin")
    def delete_database(user_role):
        return "✅ Database deleted."

    @delay(2)
    def say_hello():
        print("Hi after delay!")

    @skip_if_false(condition=False)
    def important_task():
        print("Running important task...")

    @to_uppercase
    def welcome_message(name):
        return f"Welcome, {name}"

    # Testing
    print("→", square_root(16))
    print("→", square_root(-5))
    greet()
    print("→ Fibonacci(10):", fibonacci(10))
    print("→", delete_database("admin"))
    print("→", delete_database("user"))
    say_hello()
    important_task()
    print("→", welcome_message("Ahtasham"))
    print("→ Multiply Result:", multiply(5, 4))
