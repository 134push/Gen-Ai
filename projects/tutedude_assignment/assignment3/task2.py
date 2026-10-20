def factorial(n):
    if n < 0:
        return "Invalid input (Factorial is not defined for negative numbers)"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(f"Factorial of 5 is: {result}")

result = factorial(0)
print(f"Factorial of 0 is: {result}")

result = factorial(-3)
print(f"Factorial of -3 is: {result}")
