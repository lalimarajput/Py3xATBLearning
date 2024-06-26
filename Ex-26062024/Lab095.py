
class Student:

    def __init__(self):    #constructor
        self.name = input("Enter the name:\n")
        self.age = int(input("Enter the age:\n"))

    def display(self):     #method
        print(f"Name is {self.name}, Age is {self.age}")



student = Student()   #object= calling class: Student
student.display()     #object= calling method: display
