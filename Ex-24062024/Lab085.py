#Recursion
#It is a programming technique where a function calls itself in order to solve the problem
#1.Base cae
#2.Recursive case

#Print factorial of 5:-

def factorial(n):

    if n==0 or n==1:    #Base case
        return 1
    else:
        return n*factorial(n-1)   #Recursive case

print(factorial(5))  #gives 120