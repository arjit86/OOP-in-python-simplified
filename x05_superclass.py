#super() or __init__() is used to acess the methods of a super class in a derived class
class Person (): 
    country = "Nepal"

    def takeBreath (self): 
        print ("I am breathing")

class Employee (Person): 
    company = "Softwarica"

    def getSalary(self): 
        print (f"The salary is {self.salary} ")

    def takeBreath (self):
        super().takeBreath() 
        print ("I am a employee taking a breath")

class Programmer (Employee): 
    company = "Fiverr"

    def getSalary(self):
        print ("I am taking some salary")

    def takeBreath(self): 
        super().takeBreath()
        print ("I am breathing ++")

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
pr.takeBreath()

#note all the superclasses will run in the abpoove program since  it prints the 
#corresponding superclasses as well
