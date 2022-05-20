"""
Write a class complex to represent complex numbers , 
along with the overloaded operators + and *  which adds 
and multiplies them


"""
class Complex : 
    def __init__ (self,r,i):
        self.real =  r
        self.image = i 

    def __add__ (self,c): 
        return Complex(self.real + c.real , self.image + c.image)

    def __mul__(self,c):
        return Complex(self.real * c.real, self.image * c.image) 
        
    def __str__(self): 
        return (f"{self.real} + {self.image}i")


c1 = Complex(1,4)
c2 = Complex(8,5)
print (c1 + c2)
print (c1*c2)