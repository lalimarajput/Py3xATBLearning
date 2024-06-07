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