# Label the program written in problem 4 with comments.
import os

#Select the directory whose content you want to list 
directory_path ="/"

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the content of the directory
print(contents)