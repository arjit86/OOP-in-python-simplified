class Employee: 
    company = "camel"
    location = "ktm"
    salary = 100

    # def changeSalary(self,newS): 
    #     self.__class__.salary = newS
    #     print (f"The salary is {self.salary}")

    #or 
    @classmethod
    def changeSalary(cls,newS):
        cls.salary = newS
        print (f"The salary is {cls.salary}")

e = Employee()
e.changeSalary(10000)
print (e.salary)
print("The class attribute of the salary has been changed into ",Employee.salary)

#The above program is of changing the clss attributes
# Employee.salary = 999
# print(Employee.salary)
