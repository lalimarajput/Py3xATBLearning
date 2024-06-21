#tuple can not be changed as they are immutable in nature
#hence to change any value in tuple, convert it into list

t=(1,2,3,5,6)
my_list=list(t)  #convert tuple to list
print(my_list)
my_list.append(7)   #append in list
new_list=tuple(my_list)    #pass my_list to a new list
print(new_list)