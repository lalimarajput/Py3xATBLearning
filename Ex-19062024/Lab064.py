#double the value of list elements:-

list=[1,2,3,4]
temp_list=[]   #to store the double values, creating a temporary list

for i in list:
    temp=i*2
    temp_list.append(temp)   #append() is used because we are changing the list values
    print(temp_list)

