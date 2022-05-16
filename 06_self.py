class Employee(): 
    company = "Google"
    def getSalary(self): #self is used since arjit parameter was given
        print ("salary is 100k ")

arjit = Employee()
arjit.getSalary()
#or 
Employee.getSalary(arjit) #arjit parameter is given
#self is a paramter that passes automatically in a object