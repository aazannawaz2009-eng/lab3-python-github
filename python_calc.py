def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

def percentage(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return (a / b) * 100


while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "7":
        print("Goodbye!")
        break
    elif choice == "5":
        n = int(input("Enter a number: "))
        print(n, "is", even_odd(n))
    elif choice in ["1", "2", "3", "4", "6"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "6":
            print("Result:", percentage(a, b), "%")
    else:
        print("Invalid choice")
