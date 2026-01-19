# Program to generate Fibonacci series using user input

def fibonacci(n):
    """Generates Fibonacci series up to n terms"""
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series

# User input
terms = int(input("Enter number of terms: "))

# Output
print("Fibonacci Series:")
print(fibonacci(terms))
