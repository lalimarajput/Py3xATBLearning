#OOPS-Object Oriented Programming- close to the real world
#1.Attributes- properties/data member
#2.Behaviour- Methods/Functions

#e.g.1
class Person:
#Attributes
 name=None
 id=None
 age=None
 Phone=None

#Behaviour/methods
 def walk(self):    #No arg, 1 return
    print("I am walking")
    return "I am walking"

 def another(self,name):   #1 arg, No return
    print("I am a method",name)

 def sleep(self,name):   #1 arg, 1 return
    print("sleep", name)
    return None

 def talk(self):  #no arg,no return
    print("I can talk")


#Create object
surya=Person()
surya.name="Surya prakash"
surya.talk()

ritika=Person()
ritika.name="Ritika Gupta"
ritika.walk()



