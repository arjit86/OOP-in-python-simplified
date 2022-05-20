class Sum : 
    def __init__(self,num1): 
        self.num1 = num1

    def __add__(self,num2): 
        return self.num1 + num2.num1 

a = Sum (10)
b = Sum (10)
sum = a + b 
print (sum)        