# Multilevel Inheritance:- Grandparent-->Parent-->child

class Grandparent:
    key_gold = "1kg"

    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"


class Child(Parent):
    mac_m3_apple = "M3 Max"

    def child_method(self):
        return "Child's method"


child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
print(child.key_gold)
print(child.mac_m3_apple)

parent = Parent()
parent.parent_method()
parent.grandparent_method()
print(parent.key_gold)

grandparent_ref = Grandparent()
grandparent_ref.grandparent_method()
print(grandparent_ref.key_gold)
