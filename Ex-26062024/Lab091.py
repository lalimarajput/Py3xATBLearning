class Dog:
    name = None
    id = None

    def __init__(self):  #no argument in constructor
        print("Default No Argument")

    def __init__(self, name=None, id=None):   #with argument
        self.name = name
        self.id = id

    def sleep(self):
        print("sleeping")


dog1 = Dog("Chow","1")    #object dog1= calling class Dog
dog2 = Dog()
print(dog1.name)
print(dog1.id)