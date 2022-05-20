class Person (): 
    country = "Nepal"

    def takeBreath (self): 
        print ("I am breathing")

class Employee (Person): 
    company = "Softwarica"

    def getSalary(self): 
        print (f"The salary is {self.salary} ")

    def takeBreath (self): 
        print ("I am a employee taking a breath")

class Programmer (Employee): 
    company = "Fiverr"

    def getSalary(self):
        print ("I am taking some salary")

    def takeBreath(self): 
        print ("I am breathing ++")

p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
print (pr.country)