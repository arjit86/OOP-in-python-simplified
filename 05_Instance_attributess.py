class Employee(): 
    salary = "123 k"
    company = "google"

arjit = Employee()
arjit.salary = "100 k "
arjit.age = 22 

print (arjit.salary)
print (arjit.age)

#Note the 123 k salary will not be printed since 
#instance attribute will be taken first 