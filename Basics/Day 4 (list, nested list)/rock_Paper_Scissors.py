import random

choose= int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors : "))

choice=(random.randint(0,2))

if choose == 0:
    print("You choose Rock.")
    if choice == 0:
        print("Computer's choice rock.")
        print("________________________")
        print("Draw")
    elif choice == 1:
        print("Computer's choice Paper.")
        print("_______________________")
        print("Computer Wins")
    else:
        print("Computer' choice Scissors.")
        print("_______________________")
        print("you Win")

elif choose == 1:
    print("You Choose Paper.")
    if choice == 0:
        print("Computer's choice rock.")
        print("________________________")
        print("You Win")
    elif choice == 1:
        print("Computer's choice Paper.")
        print("_______________________")
        print("Draw")
    else:
        print("Computer' choice Scissors.")
        print("_______________________")
        print("Computer Win")

elif choose == 2:
    print("You choose Scissors")
    if choice == 0:
        print("Computer's choice rock.")
        print("________________________")
        print("Computer Wins")
    elif choice == 1:
        print("Computer's choice Paper.")
        print("_______________________")
        print("you win")
    else:
        print("Computer' choice Scissors.")
        print("_______________________")
        print("Draw")

else:
    print("Not a valid number")


# second simple way
#
# import random
#
# user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
# computer_choice = random.randint(0, 2)
#
# print(f"Computer choose {computer_choice}")
#
# if user_choice > 2 or user_choice < 0:
#     print("Not valid number")
#
# elif user_choice == computer_choice:
#     print("Draw")
#
# elif user_choice == 0 and computer_choice == 2:
#     print("You win")
#
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
#
# elif computer_choice > user_choice:
#     print("You lose")
#
# else:
#     print("You win")