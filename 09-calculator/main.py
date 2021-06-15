from replit import clear
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        will_continue = input(f"Type 'y' to continue calculation with {result} or type 'n' to start a new calculation:  ")

        if will_continue == "y":
            num1 = result
        else:
            should_continue = False
            clear()
            calculator()

calculator()
