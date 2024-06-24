#apply filter to get num is greater than 5

numbers=[1,2,3,4,5,6,7,8,9,10]
def is_greater_5(num):
    return num>5

new_num_five=filter(is_greater_5,numbers)
print(list(new_num_five))