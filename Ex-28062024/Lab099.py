
class Car:
    name = None

    def __init__(self):
        self.public_var = "public"     #publec variable
        self._protected_var = "protected123"   #_ means protected variable
        self.__private_var = "pass@123"   #__ means private variable

    def __private_method(self):    #private method= only allows to be access within the class
        print("Protected!")

    def printName(self):     #public method= calling private variable
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")

# This is end of the class

alto = Car()
alto.printName()
# alto.__private_variable
