class Employee:
    language = "Python" # This is a class attribute 
    salary = 1200000

    def getInfo(self):
        print (f"This language is {self.language}. The salary is {self.salary}")


def greet(self):
        print("good morning")

@staticmethod
def greet():
        
        
        print("Good morning")
        harry = Employee()
        harry.language = "Javascript" # This is an instance attribute 
        harry.getInfo()
        harry.greet()
        # Employee.getInfo(harry)