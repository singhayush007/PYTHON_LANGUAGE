# Create a class "Programmer" for storing information of few programmers working at microsoft.

class programmer :
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name 
        self.salay = salary
        self.pin = pincode

        p = programmer ("Harry" , 1200000 , 245001)
        print (p.name, p.salary, p.pin,p.company)

        r = programmer ("Rohan" , 1200000, 245001)
        print(r.name, r.salary,r.pin,r.company)

