#Single inheritance occurs only when the child class inherits only a single parent class 
# Base class >> Derived classs 
class Employee (): 
    company = "google"
    def Infoget (self): 
        print("This is an employee class")
    def getInfo (self): 
        print ("This is an employee")

class Programmer (Employee): 
    language = "python"
    def getLanguage (self): 
        print (f"The language is {self.language}")

    def getInfo (self): 
        print ("This is a programmer ")
    
e = Employee()
e.getInfo() #prints This is an employee

p = Programmer()
p.getInfo()#An example of overwriting 
p.Infoget()#prits (This an employee class) since it has attributes of class employee
print (p.company)


#example of single inheritance 

print("_____________________________________________________________")
print ("Print example 2 ")

class Person (): 
    def personInfo (self): 
        print("I am a person")

    def personName (self): 
        print ("Hello my name is arjit")

class Student (Person): 
    def studentInfo (self): 
        print("Hello , I am a student")

    def rollNo (self): 
        print ("Hello my roll no is 7")

x = Student ()
x.studentInfo()
x.rollNo()
x.personInfo()
x.personName()

