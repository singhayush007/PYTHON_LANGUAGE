# Create a class "Employee" and add salary and increment properties to it.
# Write a method "salary Increment " method with @ property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 234
    increment = 20
    @property
    def SalaryAfterIncrement(self):
        return(self.salry + self.salary * (self.increment/100))
    
    @SalaryAfterIncrement.setter
    def salaryAfterIncrement(self , salary):
        self.increment = ((salary/self.saalry) -1)*100


e = Employee()
# print(e.SalaryAfterIncrement)
e.salaryAfterIncrement = 280
print(e.increment)


