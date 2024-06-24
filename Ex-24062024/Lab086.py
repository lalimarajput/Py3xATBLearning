#Leetcode-find sum of digits:-

number = 12345

r1 = number % 10  #Rem=5=r2
q1 = number // 10  #Quotient=1234=q2
print(r1)
print(q1)

r2 = q1 % 10  #4
q2 = q1 // 10  #123
print(r2)
print(q2)

r3 = q2 % 10  #3
q3 = q2 // 10  #12
print(r3)
print(q3)

r4 = q3 % 10  #2
q4 = q3 // 10  #1
print(r4)
print(q4)

r5 = q4 % 10  #0
q5 = q4 // 10  #1
print(r5)
print(q5)

print(r1 + r2 + r3 + r4 + r5)  #gives 1+2+3+4+5=15

#or using Recursion:-
n = 12345
def sum_of_digits(n):

 if n < 10:  #Base case
    return n
 else:
    return n % 10 + sum_of_digits(n // 10)    #Recursive case

print(sum_of_digits(12345))   #gives 15
