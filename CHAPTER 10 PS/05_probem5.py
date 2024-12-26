# Write a class Train which has methods to book a ticket, get status (no  seats) and get fare information of train running under indian railways.

from random import randit 

class Train :
    def __init__(self, trainNo):
       self.trainNo = trainNo
    def book(self,fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
            

    def getStaus(self):
      print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
       print(f"Ticket fair in train no:{self.trainNo} from {fro} to {to} is {randit (222, 5555)}")

       t = Train(12399)
       t.book('Rampur' , "Delhi")
       t.getStatus()
       t.getFare("Rampur" , "Delhi")


