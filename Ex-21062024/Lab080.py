my_dict={'a':1,'b':2,'c':3,'a':95}
print(my_dict)         #{'a': 95, 'b': 2, 'c': 3}, a will assign it's last value i.e. 95
print(len(my_dict))    #3
print(list(my_dict.keys()))    #a,b,c
print(list(my_dict.values()))   #95,2,3

for i in list(my_dict.values()):
    print(i)   #gives 95 2 3

for k,v in my_dict.items():    #to print both keys and values together
    print(k,v)

#dict will not keep the order of insertion
#OrderedDict is used to keep the order of insertion
