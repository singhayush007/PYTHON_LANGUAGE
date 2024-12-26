class Employee :
    language = "Python" # This is a class attribute
    salary = 1200000

    harry = Emplyoyee() # type: ignore
    # harry.language = "Javascript" # This is an instance attribute  
    print (harry.language , harry.salary)
