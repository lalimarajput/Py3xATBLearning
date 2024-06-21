set1={1,2,3,4,5}
set2={2,3,5}
subset=set2.issubset(set1)   #gives True because set2 is a subset of set1
print(subset)

set1={1,2,3,4,5}
set2={2,3,6}
subset=set2.issubset(set1)   #gives False because set2 is not a subset of set1
print(subset)