# Simple Calculator using functions and user input

def calculator(a, b, operator):
    """Performs arithmetic operations based on user choice"""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Display result
print("Result:", calculator(num1, num2, op))
