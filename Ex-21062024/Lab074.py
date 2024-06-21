set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set=set1.union(set2)    #returns all values of set1 and set2 {1,2,3,4,5,6,7,8}
print(my_set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set=set1.intersection(set2)    #returns common values of set1 and set2 {4,5}
print(my_set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set=set1.difference(set2)    #returns difference values of set1 from set2 {1,2,3}
print(my_set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set=set2.difference(set1)    #returns difference values of set2 from set1 {6,7,8}
print(my_set)