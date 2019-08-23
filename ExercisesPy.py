import re
import random

maxGuesses= 10                  #if ==0 lose
words= ["dwarves", "lord", "audition", "nougat", "zebra", "Spock"] #list of words; editable whenever
txt= "You now have {} more guess/es!"
failed= int


y= random.choice(words)         #choose some word from list
ite= iter(y)                    #split word into iterations

print("Input a letter !!CASE SENSITIVE!!")

x= input()                      #user input of letter
letter_found= y.find(x)
def show():                     #function used to print the index of where the input is in the word
    print(letter_found)

while maxGuesses > 1:
    failed==0                   #variable for failure
    if x in y:                  #what to do if input exists in word
        show()                  #show the location of input in word
        print("Good, go again!")
        x= input()              #input next letter

    elif x not in y:
        maxGuesses -= 1         #goes down if you get it wrong
        print("Whoops!")
        print(txt.format(maxGuesses))
        x=  input()

    if failed == 1:             
        print("You LOSE!")
        break
