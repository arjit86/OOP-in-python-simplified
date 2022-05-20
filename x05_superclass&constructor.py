#super() or __init__() is used to acess the methods of a super claass in a derived class
#we can use the constructor with the superclass
class Person (): 
    country = "Nepal"

    def __init__(self): 
        print ("Initializig the person ....\n")

    def takeBreath (self): 
        print ("I am breathing")

class Employee (Person): 
    company = "Softwarica"

    def __init__(self): 
        super().__init__()
        print ("Initializig the Employyeee....\n")

    def getSalary(self): 
        print (f"The salary is {self.salary} ")

    def takeBreath (self):
        super().takeBreath() 
        print ("I am a employee taking a breath")

class Programmer (Employee): 
    company = "Fiverr"

    def __init__(self): 
        super().__init__()
        print ("Initializig the Programmer....\n")

    def getSalary(self):
        print ("I am taking some salary")

    def takeBreath(self): 
        super().takeBreath()
        print ("I am breathing ++")

# # p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()


