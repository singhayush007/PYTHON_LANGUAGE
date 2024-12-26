class Employee:
    name = "Harry"
    language ="Py" # This is a class attribute
    salary = "1200000"

    
    harry = Employee()  # type: ignore
    harry.name = "Harry" # This is an instances  attribute 
    print(harry.language , harry.salary)

    rohan = Employee() # type: ignore
    rohan.name = "Rohan Roro Robinson" # This is an instance attribute 
    print(rohan.name , rohan.salary, rohan.language)


    # Here name is instance  attribute and salary and language are class attributes as thy directly belong to the class 
    