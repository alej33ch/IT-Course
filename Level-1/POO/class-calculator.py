class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Cannot divide by zero")


calc = Calculator()

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Select an operation (1-5): ")
    if choice == "5":
        print("Exiting the calculator. Goodbye! :)")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if choice == "1":
        print(f"The result of adding {num1} and {num2} ist: {calc.add(num1, num2)}")
    elif choice == "2":
        print(f"The result of subtracting {num2} from {num1} is: {calc.subtract(num1, num2)}")
    elif choice == "3":
        print(f"The result of multiplying {num1} and {num2} is: {calc.multiply(num1, num2)}")
    elif choice == "4":
        result = calc.divide(num1, num2)
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Invalid choice. Please select a valid option.")
