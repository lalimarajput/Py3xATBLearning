# Factorial :
def factorial(n):
    if n < 0:
        return "Invalid input, n should be a non-negative integer"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")