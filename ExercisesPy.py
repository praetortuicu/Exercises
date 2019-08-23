import re
import random

maxGuesses= 10                  #if ==0 lose
words= ["dwarves", "lord", "audition", "nougat", "zebra"]
txt= "You now have {} more guess/es!"
failed= int


y= random.choice(words)         #choose some word from stash
ite= iter(y)                    #split word into iterations
print("Input a letter !!CASE SENSITIVE!!")
x= input()                      #user input of letter

while maxGuesses >= 0:
    failed==0                   #variable for failure

    if x in y:                 #check if input is in word
        print("Good, go again!")
        x= input()
    elif x not in y:
        maxGuesses -= 1         #goes down if you get it wrong
        print("Whoops!")
        print(txt.format(maxGuesses))
        x=  input()

    if failed == 1:             
        print("You LOSE!")
        break
