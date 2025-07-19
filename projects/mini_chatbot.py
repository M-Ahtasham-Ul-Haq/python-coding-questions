"""
🤖 Mini Chatbot in Python
Features:
- Time-based greeting
- Predefined responses
- Date and time reporting
- Math evaluation
- User memory (stores name)
- Handles unknown input
"""

import datetime
import os

USERNAME_FILE = "user_name.txt"

# Function to get stored user name
def get_user_name():
    if os.path.exists(USERNAME_FILE):
        with open(USERNAME_FILE, 'r') as file:
            return file.read().strip()
    return None

# Function to set user name
def set_user_name(name):
    with open(USERNAME_FILE, 'w') as file:
        file.write(name)

# 1. Greet user with time-based message
def time_based_greeting(name=None):
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    if name:
        return f"{greeting}, {name}!"
    else:
        return f"{greeting}! What's your name?"

# 2–9. Main response function
def respond(user_input):
    user_input = user_input.lower().strip()

    if "how are you" in user_input:
        return "I'm just a bot, but I'm doing great. How can I help you?"

    elif "who are you" in user_input:
        return "I'm your mini chatbot assistant."

    elif "date" in user_input or "time" in user_input:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current date and time is {now}."

    elif "celsius to fahrenheit" in user_input:
        try:
            temp = float(input("Enter Celsius temperature: "))
            fahrenheit = (temp * 9/5) + 32
            return f"{temp}°C is {fahrenheit:.2f}°F."
        except ValueError:
            return "Please enter a valid number."

    elif "joke" in user_input:
        return "Why did the Python developer go broke? Because he couldn't catch an exception!"

    elif any(op in user_input for op in ['+', '-', '*', '/']):
        try:
            result = eval(user_input)
            return f"The result is {result}."
        except:
            return "Sorry, I couldn't calculate that."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I didn't understand that."

# 10. Organize chatbot session
def mini_chatbot():
    name = get_user_name()
    print(time_based_greeting(name))

    if not name:
        name = input("What's your name? ").strip()
        set_user_name(name)
        print(f"Nice to meet you, {name}!")

    while True:
        user_input = input(f"{name}: ")
        response = respond(user_input)

        print(f"Bot: {response}")

        if "goodbye" in response.lower():
            break

if __name__ == "__main__":
    mini_chatbot()
