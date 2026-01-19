# Program to check whether a number is prime

def is_prime(n):
    """Returns True if number is prime, else False"""
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# User input
num = int(input("Enter a number: "))

# Output
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")
