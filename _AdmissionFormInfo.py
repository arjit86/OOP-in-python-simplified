class AdmissionFormInfo (): 
    seats = 10
    
    def __init__ (self,name,classs): 
        self.name = name 
        self.classs = classs

    def printName (self): 
        print (f"The name of the student is {self.name}")

    def printClass (self): 
        print (f"The student have just passed from grade {self.classs}")

    def admissionInfo (self): 
        if self.classs == 10 : 
            print ("You can apply for the form")
        else : 
            print("Sorry you must pass grade 10 to fill the form")

    def bookSeat (self): 
        if self.classs == 10 : 
            print ("your seats have been booked")
            AdmissionFormInfo.seats = AdmissionFormInfo.seats - 1 
        else :
            print("You can't book the seats for college")

student = AdmissionFormInfo("arjit", 10)
student.printName()
student.printClass()
student.admissionInfo()
student.bookSeat()
print ("Printing the class attribute after booking a seat")
print (AdmissionFormInfo.seats)