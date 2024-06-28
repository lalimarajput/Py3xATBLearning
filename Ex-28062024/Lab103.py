
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):    #public method/function calling pvt var
        print(self.__private_var)

    def deposit(self, amount):    #public method calling public var
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Your Balance is ", self.balance)

jp_chase = BankAccount()    #jp_chase= bank name
print(jp_chase.balance)  #o/p=0
jp_chase.deposit(101)
jp_chase.show_balance()  #o/p= Your balnce is 101
jp_chase.deposit(99)
jp_chase.show_balance()  #o/p=Your Balance is  200
jp_chase.withdraw(199)
jp_chase.show_balance()  #o/p=Your Balance is  1

#This is a bad example for bank withdrawal and show balance to everyone
#rather we should use encapsulation to authenticate user