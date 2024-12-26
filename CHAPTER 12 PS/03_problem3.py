# Write a list comprehesions to print a list which contains the multiplications table of a  user entered number.

n = int(input("Enter the number:"))


table = [n *1  for i in range (1 , 11)]
print(table)