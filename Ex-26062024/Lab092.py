class Calc:

    def __init__(self):   #define constructor without arguments
        print("Hello DC")

    def sum(self,a,b):   #define method with arguments
        return a+b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()                   #object= calling class: Calc
output = object_ref.sum(3,4)    #object= calling method: sum
print(output)