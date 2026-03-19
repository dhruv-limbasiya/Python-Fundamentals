print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')

print("Welcome to Treasure Island")
choice=input("you are in crossroad would you liek to go right or left? type 'r' for yes or 'l' for no: ")
if choice=="R" or choice=="r":
    print("Game Over")
elif choice == "l" or choice =="L":
    print("you are in beach.")
    wants=input("Would you like to swim to the island or wait for boat? type 'w' for wait or 's' for swim: ")
    if wants == "S" or wants =="s":
        print("Game Over")

    elif wants=="w" or wants=="W":
        print("you are in castel")
        choose=input("Which door you wants to choose? type 'r' for red or 'b' for blue or 'y' for yellow: ")
        if choose == "R" or choose == "r":
            print("Game over")
        elif choose == "b" or choose == "b":
            print("Game over")
        elif choose == "y" or choose == "Y":
            print("You Win the game")
        else:
            print("Not Valid Input")
    else:
        print("Not Valid Input")
else:
    print("Not valid Input")
