# Write a program to print the multiplication table of n using for loops in reserved order.

n =int(input('Enter the number:'))

for i in range(1,11):
    print(f"{n} x {11-i} = {n*{11-i}}")