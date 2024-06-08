# List
my_list = [1,2,3]

my_list.append(4)  # append() is use to add a single element at the end of the list
print(my_list)

my_list.extend([4,5])  # extend() is use to add all elements at the end of the list
print(my_list)

my_list.insert(1,'a') # insert() is use to add a element to a specific position
print(my_list)

my_list.remove(2)
print(my_list)  # remove() is use to remove the first occurence of a specified value/element of the list


item = my_list.pop(1)  # pop() is use to remove the lst item
print(item)
print(my_list)

my_list.clear()  # To clear the list
print(my_list)

my_list = [1,2,3,2]    # returns index of first occurence of a specific number
item = my_list.index(2)  # index of 1 is 0 ,index of 2 is 1, index of 3 is 2....
print(item)  #o/p = 1

my_list = [1,2,3,2]
item = my_list.count(2)  # returns count of the specific number
print(item)  #o/p = 2

my_list = [3,1,2]
my_list.sort()  # sort in ascending order by default
print(my_list)   # o/p = [1,2,3]

my_list = [1,2,3]
my_list.reverse()  # returns reverse order of the list
print(my_list)

my_list = [1,2,3]    # len() is a built-in function same as input() function
length = len(my_list)  # returns length of the list
print(length)   # o/p = 3



