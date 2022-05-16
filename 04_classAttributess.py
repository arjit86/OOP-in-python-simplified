class Employee(): 
    company = "google"
arjit = Employee()
print(arjit.company) #prints Google 
Employee.company = "Youtube" #changing the class attribute
print(arjit.company)