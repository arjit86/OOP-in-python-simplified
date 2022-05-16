"""
Examples of __init__ functions takking the self arguments


""" 
class Employee(): 
    def __init__ (self,name,age,salary): 
        self.name = name
        self.age = age
        self.salary = salary
        print (f"Hello {self.name}")
    
    def getInfo(self): 
        print (f"The name of the employee is {self.name}")
        print (f"The age  of the employee is {self.age}")
        print (f"The salary of the employee is {self.name}")

arjit = Employee("arjit","22","12LPa")
arjit.getInfo()