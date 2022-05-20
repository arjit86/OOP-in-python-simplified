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
p.getInfo() 
p.Infoget()#prits (This an employee class) since it has attributes of class employee
print (p.company)