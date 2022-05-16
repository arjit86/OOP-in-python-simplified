#wap to store some data of the programmers working at microsoft 
class Employee (): 
    company = "Microsoft"

    def __init__(self,name,age,salary):
        self.name = name 
        self.age = age 
        self.salary = salary

    def proInfo (self): 
        print (f"The name of the programmer is {self.name}")
        print (f"The age of the programmer is {self.age}")
        print (f"The salary of the programmer is {self.salary}")

programmer = Employee ("Arjit","22","1LPA")
programmer2 = Employee("Suzu","24","2 LPA")


programmer.proInfo()
programmer2.proInfo()