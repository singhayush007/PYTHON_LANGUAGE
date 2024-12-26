# The game() function in a program lets a user play a game and return the score as an integer. You need to read a file `Hi-score.txt`. Which is either blank or contains the previous score Hi score. You need to write  aptogram to update the Hi score whenever the game() function breaks the Hi-score.
import random

def game():
  print("You are playing the game..")
  
  score =random.randit(1,62)
  # Fetch hisscore 
  with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore!=""):
       hiscore = int(hiscore)
    else:
       hiscore =0
       
       print(f"Your score : {score}")
       if(score>hiscore):
       # Write this hiscore to the file 
          with open("hiscore.txt" , "w") as f:
             f.write(str(score))

       return score 

       game()

    