#WAP to determine whether the given year is a leap year:

#A year is a leap year if:
#It is divisible by 4.
#If it is divisible by 100, it must also be divisible by 400 to be considered a leap year.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")