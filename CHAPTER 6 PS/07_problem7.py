# Write a program to find out whether a given post is talking about "Harry" or not.


post = "Hey harry bhai is good harry is very good and harry is great"

if ("Harry.lower() in post.lower()"):
    print("This post is talking about harry")

else:
    print("This is not talking about harry")