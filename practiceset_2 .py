#Wap to write a class calculator to find square , cube and square root
class Calculator(): 
    def __init__(self,a): 
        self.a = a 

    def square(self): 
         print(f"The square is {self.a * self.a}" )

    def cube (self): 
        print(f"The cube is {self.a ** 3}")

    def squareroot(self): 
        print (f"The square root is {self.a ** 0.5}")

a = int(input("Enter any no : "))
number = Calculator(a)
number.square()
number.cube()
number.squareroot()