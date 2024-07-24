
class MyCustomException(Exception):   #we can make our own exception
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount!"))
if withdraw > balance:
    raise MyCustomException("Bal is Low!!")
else:
    print("Remain Bal ", (balance - withdraw))