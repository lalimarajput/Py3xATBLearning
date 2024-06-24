#Filter:-
#Allow you to filter elements in list,tuple and set

numbers=[1,2,3,4,5,6,7,8,9,10]
#apply even filter on the above

def is_even(num):
    return num%2==0   #if num is divided by 2 and rem is 0 then it is even num

new_num_even=filter(is_even,numbers)
print(list(new_num_even))    #o/p=[2,4,6,8,10]
#converting to list to get the exact output