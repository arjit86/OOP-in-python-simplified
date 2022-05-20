class Employee (): 
    company = "Google"
    salary = 1200
    bonus = 200

    @property #example of getter
    def totalSalary (self): 
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.bonus = val - self.salary 

e = Employee()
print (e.totalSalary)
e.totalSalary = 1900
print (e.salary)
print (e.bonus)