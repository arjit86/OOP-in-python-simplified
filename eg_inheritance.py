class Husband (): 
    surname = "magar"

    def headofHouse (self): 
        print ("I am the husband as  head of the house")

    @staticmethod
    def roleofFather () : 
        print ("I am husband and i play the role of father")

class Wife (): 
    surname = "******"

    def headofHouse(self): 
        print ("I am wife as the head of the house ")

    @staticmethod 
    def roleofMother (): 
        print ("I am wife and i play the role of mother")

class Child (Wife,Husband): 
    #since the Husband is kept first the superclass is husband 
    
    def headofHouse(self): 
        
        super().headofHouse()
        print ("I am just a child and not the head of the house ")
    
    def __init__ (self,name): 
        self.name = name

    def childInfo (self):
         print(f"My name is {self.name}")

child = Child ("Antonio")
child.childInfo()
print("My surname is ",child.surname)
child.roleofFather()
child.roleofMother()
child.headofHouse()