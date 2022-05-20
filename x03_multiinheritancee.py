class Employee() : 
    company = "google" 
    ecode = "A2ADN"

class Freelancer (): 
    company = "Fiverr"
    level = 0

    def upgradeLevel(self): 
        self.level = self.level + 1 

class Programmer (Employee,Freelancer): 
    name = "Arjit"

p = Programmer()
p.upgradeLevel()
print (p.level)
print (p.company) #google will be printed since employee class comes first 

print ("_________________________________________________________________________________")
print ("Examplee 2 ")
class Person(): 
    name = "Arjit"
    age = 22
class Student (): 
    college = "kist"
    rollno = 7 
class Employee (Person,Student): 
    job = "programmer"
    salary = "no salary for noobs"

a = Employee()
print (a.name)
print (a.age)
print (a.college)
print (a.job)
print(a.salary)