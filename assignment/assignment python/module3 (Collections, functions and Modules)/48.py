
# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
number = 6
print(f"The factorial of {number} (recursive): {factorial_recursive(number)}")
print(f"The factorial of {number} (iterative): {factorial_iterative(number)}")