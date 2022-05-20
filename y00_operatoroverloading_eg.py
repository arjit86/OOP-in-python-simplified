class Arjit : 
    def __init__(self,a): 
        self.a = a 

    def __add__(self,b): 
        return self.a + b.a 

    def __str__(self):
        return f"{self.a}"

a = Arjit(20)
b = Arjit(20)
print (a)