# Write a program to input name, marks and phone number of a student and format it using the frmat functions like below:

# "The name of the student is Harry, his marks are 72 and phone number is 99999888"


name  = input("Enter name:")
marks = int(input("Enter marks:"))
phone = int(input("Phone number:"))

s = "The name of the student is {}, his marks{} and phone number is {} .format(name , marks, phone)."

print(s)
