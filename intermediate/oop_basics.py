"""
📘 Python OOP Basics Practice
This script includes 11 beginner-to-intermediate object-oriented programming exercises
to demonstrate class design, inheritance, encapsulation, class methods, and more.
"""

# 1. ✅ Create a Person class with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 2. ✅ Create Student class with grades and methods
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # list of grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# 3. ✅ Inherit Employee from Person and calculate salary
class Employee(Person):
    def __init__(self, name, age, hourly_rate, hours_worked):
        super().__init__(name, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# 4. ✅ Add __str__ and __repr__ methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

# 5. ✅ Use getters and setters for encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

# 6. ✅ Demonstrate class and instance variables
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # modifies class variable
        self.id = Counter.count  # instance variable

# 7. ✅ Implement a class with class method and static method
class Utility:
    version = "1.0"

    @classmethod
    def get_version(cls):
        return cls.version

    @staticmethod
    def greet(name):
        return f"Hello, {name}!"

# 8. ✅ Create a BankAccount class with deposit/withdraw
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

# 9. ✅ Implement constructor chaining
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # constructor chaining
        self.model = model

# 10. ✅ Create multiple objects and compare them
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# 11. ✅ Use __del__ method and explain garbage collection
class TempFile:
    def __init__(self, name):
        self.name = name
        print(f"Temporary file {self.name} created.")

    def __del__(self):
        print(f"Temporary file {self.name} deleted (garbage collected).")

# === Example Usage ===
if __name__ == "__main__":
    # Person & Student
    p = Person("Ali", 30)
    s = Student("Sara", [90, 80, 95])
    print("Student Average:", s.average_grade())

    # Employee
    e = Employee("John", 40, 20, 160)
    print("Monthly Salary:", e.calculate_salary())

    # Book
    book = Book("1984", "George Orwell")
    print("Book:", book)
    print("Book (repr):", repr(book))

    # Account
    acc = Account(500)
    print("Balance:", acc.get_balance())
    acc.set_balance(1000)
    print("Updated Balance:", acc.get_balance())

    # Counter
    c1 = Counter()
    c2 = Counter()
    print("Instance IDs:", c1.id, c2.id)

    # Utility
    print("Version:", Utility.get_version())
    print(Utility.greet("Ahtasham"))

    # BankAccount
    my_acc = BankAccount("Ali", 200)
    my_acc.deposit(150)
    my_acc.withdraw(100)

    # Car with constructor chaining
    my_car = Car("Toyota", "Corolla")
    print("Car:", my_car.brand, my_car.model)

    # Point comparison
    p1 = Point(2, 3)
    p2 = Point(2, 3)
    print("Points Equal:", p1 == p2)

    # TempFile and garbage collection
    tf = TempFile("temp123")
    del tf  # triggers __del__ manually
