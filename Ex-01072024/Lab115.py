
# Polymorphism
# Polymorphism allows objects of
# different classes to be treated as
# objects of a common superclass.
# same object behave differently for different class

# Pramod -> Mentor, Husband, Brother.
# Object -Method -> Mother, Matenal She is, sister, parent -

#Types:-
#1.Method overriding- child always override the parent function
#2.Metho overloading- not supported in python

# Method overriding

class Shape:   #parent class
    def area(self):
        print("Area of the Shape")


class Rectangle(Shape):  #child class inherit parent class
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius



shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())


shape3 = Shape()
shape3.area()
#same object (area) will behave differently for different class
