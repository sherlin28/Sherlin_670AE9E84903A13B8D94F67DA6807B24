def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5  # Replace this with the desired number
result = factorial(number)
print(f"The factorial of {number} is {result}")