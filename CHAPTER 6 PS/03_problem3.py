# A spam commnet is defined as a text containing following keywords:
# "Mkae alot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

p1 = "Make  a lot of money "
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
      print("This comment is a spam")

else:
       print("This comment is not a spam")