# A file contains a word "Donkey" multiple times. You need to write a program h=which replace this word with #### by updating the same file.


word = "Donkey"

with open("file.txt", "read") as f:
    content = f.read ()

    contentNew = content.replace(word, "######")

    with open ("file.txt" , "write" ) as f:
        f.write(contentNew)
                                 