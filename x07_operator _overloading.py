#operators in python can be loaded using the dender methods
#these methods are called when an operators are used in  python
class Number: 
    def __init__(self,num1): 
        self.num = num
        
    def __add__(self,num2):
        print ("Lets add")
        return self.num + num2.num

    def __mul__(self,num2):
        print ("lets multiply")
        return self.num * num2.num

a = Number(12)
b = Number(20)
sum = a + b 
mult = a * b
print (sum)
print(mult)



