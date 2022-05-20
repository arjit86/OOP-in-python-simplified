#wap a class C-2d vector and use it to create another class representing 3D vector 
class C2DVec(): 
    def __init__(self,i,j): 
        self.icap=i 
        self.jcap=j 
    
    def __str__(self): 
        return f"{self.icap}i + {self.jcap}j"
        
class C3DVec (C2DVec): 
    def __init__(self,i,j,k): 
        super().__init__(i,j)
        self.kcap = k 
        
    def __str__(self): 
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2D = C2DVec(1,3)
v3D = C3DVec(1,5,6)
print(v2D)
print(v3D)