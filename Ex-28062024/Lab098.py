
class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an object is created")

    def change_password(self):
        self.password = "345"
# This is end of the class

xuv = Car()
xuv.password = "345"