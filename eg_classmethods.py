class MyName(): 
    mynumber = 9869412686
    age = 16
    
    @classmethod
    def changeNumber (self,newNum): 
        self.mynumber = newNum 
        print(f"The new number is {self.mynumber}")

    @classmethod
    def changeAge (self,newAge): 
        self.age = newAge
        print (f" My new age is {self.age}")

arjit = MyName()
arjit.changeAge(19)
arjit.changeNumber(9869412597)
print (MyName.age)
print(MyName.mynumber)