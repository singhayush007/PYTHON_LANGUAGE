# Can you change the self-paramtere inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects.

from random import randit 

class Train :
    def __init__(slf, trainNo):
       slf.trainNo = trainNo
    def book(harry,fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")
            

    def getStaus(self):
      print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
       print(f"Ticket fair in train no:{self.trainNo} from {fro} to {to} is {randit (222, 5555)}")

       t = Train(12399)
       t.book('Rampur' , "Delhi")
       t.getStatus()
       t.getFare("Rampur" , "Delhi")
