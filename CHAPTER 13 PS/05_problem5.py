# Write a program to find the maximum of the numbers in a list uisng the reduce function.

from functools import reduce

a = [111,2,65,53,53,635,65,74,45,55]

def greater (a , b):
    if(a >b):
        return a
    return b


print(reduce(greater, 1))

