#Decorators:-It is essentially a function that takes another function as an argument

def my_decorator(func):
    def wrapper():
        print("starting")
        print("*****")
        func()
        print("*****")
        print("ending")

    return wrapper()

@my_decorator
def say_hello():
    print("say hello")

#if we don't add @my_decorator then it will only print "say hello"
#no need to call "say hello", it will be autromatically called by decorator