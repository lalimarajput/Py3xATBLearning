numbers = [1, 2, 3]
a=numbers


def list(a):  # define list function
    a.append(4)
    a[0] = 100
    return a


l = list(numbers)  # calling list function
print(l)
