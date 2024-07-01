from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass


class Pramod(Father):
    def loan(self):
        print("Loan given")


pramod = Pramod("rancho")
pramod.loan()