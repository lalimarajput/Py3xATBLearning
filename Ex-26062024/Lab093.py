
class Calc:

    def __init__(self, a, b):    #constructor with arguments
        self.a = a
        self.b = b

    def sum(self):          #methods without arguments
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object_ref = Calc(3, 4)
output = object_ref.sum()
print(output)
