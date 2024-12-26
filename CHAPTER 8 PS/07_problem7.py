# Write a python function to remove a given word from a listed strip is at the same time.

def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
         n.append(item.strip(word))
    return n 
    
l = ["Harry" , "Rohan", "Shubham", "an"]
print(rem(l, "an"))