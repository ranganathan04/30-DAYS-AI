import datetime
import math
import random

def greet_user():
    print("Hello! I'm your Python AI Assistant 🤖")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

def tell_time():
    now = datetime.datetime.now()
    print(f"📅 Today's date is {now.strftime('%A, %d %B %Y')}")
    print(f"⏰ Current time is {now.strftime('%I:%M %p')}")

def solve_math():
    print("I can help you with basic math.")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print("Result:", num1 + num2)
        elif operator == '-':
            print("Result:", num1 - num2)
        elif operator == '*':
            print("Result:", num1 * num2)
        elif operator == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("❌ Cannot divide by zero.")
        else:
            print("❌ Invalid operator.")
    except ValueError:
        print("❌ Please enter valid numbers.")

def tell_joke():
    jokes = [
        "Why did the programmer quit his job? Because he didn't get arrays. 😂",
        "Why do Python devs wear glasses? Because they can't C#. 🤓",
        "Why was the math book sad? Because it had too many problems. 😅"
    ]
    print("Here's a joke for you:")
    print(random.choice(jokes))

def main():
    greet_user()
    while True:
        print("\nHow can I assist you?")
        print("1. Tell date and time")
        print("2. Solve math problem")
        print("3. Tell a joke")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            tell_time()
        elif choice == '2':
            solve_math()
        elif choice == '3':
            tell_joke()
        elif choice == '4':
            print("Goodbye! Have a great day! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
