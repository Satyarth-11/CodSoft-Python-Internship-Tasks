# Task 1: Basic Calculator

def calculator():
    print("Enter two numbers:")
    a = float(input("A: "))
    b = float(input("B: "))
    op = input("Operation (+, -, *, /): ")

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operator.")

calculator()
