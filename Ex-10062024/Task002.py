
# Develop a Python script that calculates the square and cube of a given number.
# num = 2 sq = 4, c = 8
num = 2
square = num ** 2
cube = num ** 3

print(f"The square of {num} is {square}.")
print(f"The cube of {num} is {cube}.")


# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} is {'greater than' if num1 > num2 else 'less than' if num1 < num2 else 'equal to'} {num2}.")
