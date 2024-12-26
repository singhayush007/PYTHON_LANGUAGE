# Repeat program 4 for a list of such words tobe censored.

words = [ "Donkey" , "bad" , "ganda"]

with open("file2.txt" , "read") as f:
    content = f.read()

    for word in words:
        content = content.replace(word, "#" *len(word))

        with open ("file2.txt" , "w") as f:
            f.write(content)