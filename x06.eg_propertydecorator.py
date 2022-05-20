class Employee(): 
    salary = 1000 #example of property
    bonus = 100
    
    @property 
    def totalSalary (self): 
        return self.salary + self.bonus 

    @totalSalary.setter 
    def totalSalary(self,val):
        self.bonus = val - self.salary 

e = Employee()
# print (e.totalSalary)#runs like property 
e.totalSalary = 1800
print (e.bonus)
