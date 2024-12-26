#   Write a program to open three fies 1.txt, 2.txt, 3.txt if any these files are not present , a message withut exiting the program must be printed prompting the same.

try:
    with open("1.txt" , "r") as f:
        print(f.read())
except Exception as e:
   print(e)


try:
    with open("2.txt" , "r") as f:
        print(f.read())
except Exception as e:
   print(e)


try:
    with open("3.txt" , "r") as f:
        print(f.read())
except Exception as e:
   print(e)


print("Thank you!")