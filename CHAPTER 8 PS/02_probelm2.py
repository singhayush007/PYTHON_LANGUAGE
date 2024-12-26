# Write a python program using functions to convert Celcius to fahernheit.

def f_to_c(f):
    return 5*(5-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c , 2) }Degree C ")