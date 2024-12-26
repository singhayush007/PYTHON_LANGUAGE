# Create a class with a class sattribute a; create an object from it and set 'a' directly using object. a=o . Does this change the classs ttribute.

class Demo:
    a = 4

    o = Demo() # type: ignore
    print(o.a) # Prints the class attribute because instance attribute is not present

    o.a = 0 # Instance attribute is set
    print(o.a) # Print the instance attribue beacsue instance attribute is present
    print(Demo.a) # type: ignore # Prints the class attribute