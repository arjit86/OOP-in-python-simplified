""" create a class Pets from Animals and furter create class Dog from 
the pets ..Add the methods to bark"""

class Animals : 
    type = "mammals"


class Pets (Animals): 
    color = "Black"

class Dog (Pets): 
    dogtype = "labradar"

    def bark (self): 
        print("Vow vow ")

a = Dog()
a.bark()
print(a.type)