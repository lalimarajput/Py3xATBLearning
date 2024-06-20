#even_odd function

def find_odd_even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

find_odd_even(57)
#calling find_odd_even function to check the number is odd or even

#or we can use lambda expression:-
check_even_odd=lambda num:"even"if  num%2==0 else "odd"
print(check_even_odd(66))
