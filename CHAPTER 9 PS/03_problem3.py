# Write a program to gnerate the multipliction tables from 2 to 20 and write it to the different files. Place these files in afolder for a 13- Year old.

def generateTable(n):
    table = ""
    for i in range (1, 11):
        table += f"{n} x {i} = {n*i}\n"

        with open (f"tables/table_{n}.txt", "w") as f:
            f.write(table)


for i in range (2, 21):
    generateTable(i)