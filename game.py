import time

choice_A= ["A", "a"]
choice_B= ["B", "b"]
choice_C= ["C", "c"]
yes= ["Y", "y"]
no= ["N", "n"]

sword= 0
rock= 0
health= 100
coins= 20

print("Welcome to the game! \nHope you enjoy!")

def intro():
    print("\nYou are a young knight which has been gifted magical powers...\n"
           "To free your people of the oppression of the dark realm, you must fight the endless hordes of enemies \nunleashed by the ruthless Zorga,"
           "an evil wizard. \n You come to a crossroads in a forest which way do you go? Left(A) or right(B)?")
    time.sleep(1)
    choice = input(">>> ")
    if choice in choice_A:
        print("You went left!")
        option_left_path()
    elif choice in choice_B:
        print("You went right!")
        option_right_path()

def option_left_path():
      print("You chose the darker way through the forest. Although shorter, it is also more dangerous\n"
              "After some more horse riding, a pack of gnomes attacks you. You quickly draw out your sword, but they\n"
              "manage to knock you off your horse. Do you:")
      print("A. Run towards the one with a bow and slash him to bits\n"
              "B. Stand your ground and wait for them to get closer, then take them out one by one\n"
              "C. Run away in fear.")
      choice= input(">>>")
      if choice in choice_A:
             print("You try to run towards the gnome most far away, so you get a tactical advantage over the others. In the process, the others manage to get a few hits in.\n"
                  "After some fighting, you manage to kill all of them, but you have been hurt. You climb on your horse and continue your journey.")
             health -= 25
      elif choice in choice_B:
             print("You stand your ground, waiting for them to attack. This gives you the advantage over them, so you manage\nto kill all of them without getting hurt."
                  "You loot them and find some coins. You continue your journey through the forest")
             coins += 10
      elif choice in choice_C:
          print("You choose to run away in fear. The gnomes catch up to you and kill you mercilessly.")
          die()

      enchantment= False
          
def option_right_path():
    print("You chose to go right! The elders have told you this is the longer, yet easier path through the forest.\nAfter some time, you encounter an old man."
          "He asks you for food. Do you give him any of your food?")
    choice= input(">>>y/n")
    if choice in yes:
        print("You give the man a piece of your bread and an apple. He says he will make it worth your while and tells you to follow him.\n"
              "You follow the man to what appears to be a small town that is not on your map. There, people are kind to you.\n"
              "The man tells you, you can enchant your weapons and armor, as a gift for what you did for him."
              "Later that day, you leave the town, promising to return and help the folk if ever need be.")
        enchantment= True
    elif choice in no:
        print("The man becomes pale and walks away. You feel frightened and a chill runs down your spine. You continue your way.\n")
        enchantment= False

def die():
    print("You died!\n Restart?")
    choice= input(">>>y/n")

    if choice in yes:
       intro()
    elif choice in no:
       print("OK!")

intro()