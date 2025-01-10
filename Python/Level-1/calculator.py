
# Create a calculator that can add, subtract, multiply or divide depending upon the input from the user.
def sume(a,b):
    return a + b

def rest(a,b):
    return a - b

def multi(a,b):
    return a * b

def dive(a,b):
    if b != 0:
        return a / b
    else:
        return "you can't divide by zero"


print("Select a operation: 1. Sume 2. Rest 3. Multiple 4. Divide")
operation = input("Enter the operation number: ")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "1":
    print("Result:",sume(num1, num2))
elif operation == "2":
    print("Result:",rest(num1,num2))
elif operation == "3":
    print("Result:",multi(num1,num2))
elif operation == "4":
    print("Result:",dive(num1,num2))
else:
    print("Invalid operation")