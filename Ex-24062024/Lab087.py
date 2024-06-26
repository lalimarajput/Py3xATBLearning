n=12345

def sum_of_digits(n):
    sum=0

    while n>0:
        sum = sum + n%10
        n= n//10   #gives quotient
    return sum

print(sum_of_digits(12345))   #gives 15

