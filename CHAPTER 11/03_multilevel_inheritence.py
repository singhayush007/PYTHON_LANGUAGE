class Employee:
    a = 1

    class Programmer(Employee): # type: ignore
        b = 2

        class Manager (Programmer): # type: ignore
            c = 3

            o = Employee() # type: ignore
            #print(o.a) # Prints the a attribute
            #print(o.b) # Shows an error as there is no b attribute in Employee class

            o = Programmer() # type: ignore
            print(o.a , o.b)

            o = Manager() # type: ignore
            print(o.a , o.b, o.c)
            