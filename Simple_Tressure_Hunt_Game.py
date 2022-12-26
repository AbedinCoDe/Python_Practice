print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


userInput = input('Now you have to crossing the rood. which side you wanna go? "left", "right"\n')

if userInput == "left":
    userInput1 = input('You have two choice, you can "wait" or you can "swim" for go to that side.\n')
    if userInput1 == "wait":
        userInput2 = input('Now you overtake the lake, Now you arrived to an Iland, There are three doors, "red", "blue","yellow", which one you choose?\n')
        if userInput2 == "red":
            print("Noo..You burned by fire, Game over!")
        elif userInput2 == "blue":
            print("Noo, You are bitten by trout. Game Over")
        elif userInput2 == "yellow":
            print("WOW..You Found the treasure ! You Win!")
        else:
            print("YOu choose a door that is not exist!")
    else:
        print("Oho, YOu attach by a crocodile")
else:
    print("You Fall into a hole. Game Over")
