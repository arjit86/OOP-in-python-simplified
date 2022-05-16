seatno = [1,2,3,4]
class BusTicket(): 

    def __init__(self,name,fare,seats): 
        self.name = name 
        self.fare = fare 
        self.seats = seats 
        self.i = -1

    def busInfo (self): 
        print (f"The bus name is {self.name}")
        print (f"The bus fare is Rs{self.fare}")
        print (f"The bus has seats of {self.seats}")

    def bookTicket (self):
        if self.seats > 0 :
            self.seats = self.seats - 1
            self.i = self.i + 1
            print (f"The seat has been booked and seat no is {seatno[self.i]}")
        else : 
            print("The seats have been packed")

bus1=BusTicket("LCD DELUXE",1200,4)
bus1.busInfo()
print("\n**********************************")

bus1.bookTicket()
print("1st ticket booked")

bus1.bookTicket()
print("2nd ticket booked")

bus1.bookTicket()
print("3rd ticket booked")

bus1.bookTicket()
print("4th ticket booked")

bus1.bookTicket()
#Made by me wiithout any refrences