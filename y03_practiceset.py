"""
Create a class employee and add salary with the increment properties to 
it
Write a method salary after increment method with a property decorator 
with a setter which change the value of increment based on salary

salary after increment = salaary * increment
"""
class Employee : 
    salary = 1000 
    increment = 2

    @property 
    def salaryAfterIncrement (self) : 
        return self.salary * self.increment

    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self,val): 
        self.increment = val / self.salary 

a = Employee()
print (a.salaryAfterIncrement)
a.salaryAfterIncrement = 10000 
print (a.increment)