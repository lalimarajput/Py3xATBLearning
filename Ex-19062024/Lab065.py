#or use map() function:- to double values of list without for loop and append() function

my_list=[1,2,3,4,5]
def double_item(num):
    return num*2


double_list=list(map(double_item,my_list))  #using map() function to double the values of the list
print(double_list)

#or use lambda expression:-
double_item= lambda num:num*2
print(double_item)