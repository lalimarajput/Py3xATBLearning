
# Multiple Inheritance:- child inherit from two different parents (Father and Mother)

class Father:
    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        return "This is from the Mother"


class Son(Father, Mother ):   #first one is father so, father will be printed
    pass



# Probelm - Diamond Problem - Java
# Python - Multiple Inheritance fixed diamond problem-
# if child have same function as both parents have then child's function will be used
#if both parents have same functions but child doesn't has then it will use first parent inside the child's function/method.

# F,M -> S

son = Son()
son.father_money()
son.mother_money()
print(son.home()) # Method Resolution
