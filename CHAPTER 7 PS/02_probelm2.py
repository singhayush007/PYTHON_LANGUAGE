# Write a program to greet all the person names stored in a list 'l' and which starts wih s.
# l = ["Harry", "Soham", "Sachin", "Rahul"]


l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")