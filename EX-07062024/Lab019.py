name = "Amit"
print(id(name))  # id returns the identity or memory address of the object

print(len(name))  # o/p= 4

name= name.lower()  # To print in lowercase letters
print(name)

name= name.upper()  # To print in uppercase letters
print(name)

# print(name[4])  # not allowed, gives error - string index out of range

print(name[3])  # o/p = T of Amit, index= A=0, m=1, i=2, t=3

# Python is immutable-can not be changed
name[0] = "p"  # "str" object does not support item assignment
#beacuse [0] is A in Amit not "P"

