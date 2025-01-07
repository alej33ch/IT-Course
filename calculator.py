def sum(a,b):
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

print("Select a operation: 1. Sum 2. Rest 3. Multiple 4. Divide")
operation = input("Enter the operation number: ")
