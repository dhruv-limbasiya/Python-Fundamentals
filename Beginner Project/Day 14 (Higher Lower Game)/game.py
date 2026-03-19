import random
from game_data import data

logo = """
 _    _ _____ _____ _    _ ______ _____  
| |  | |_   _/ ____| |  | |  ____|  __ \ 
| |__| | | || |  __| |__| | |__  | |__) |
|  __  | | || | |_ |  __  |  __| |  _  / 
| |  | |_| || |__| | |  | | |____| | \ \ 
|_|  |_|_____\_____|_|  |_|______|_|  \_\
 _      ____  _    _ ______ _____  
| |    / __ \| |  | |  ____|  __ \ 
| |   | |  | | |  | | |__  | |__) |
| |   | |  | | |  | |  __| |  _  / 
| |___| |__| | |__| | |____| | \ \ 
|______\____/ \____/|______|_|  \_\ """

vs = """
__      _______ 
\ \    / / ____|
 \ \  / / (___  
  \ \/ / \___ \ 
   \  /  ____) |
    \/  |_____/ 
"""


def format_data(account):
    # format the account data into printable format.
    return f"{account['name']}"


def check_ansewer(user_guess, a_followers, b_followers):
    """take s user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")

    # Ask user for guess.

    guess = input("Who have more followers? Type 'a' or 'b': ").lower()

    #clear the screen
    print("\n" *20)
    # check if user is correct.
    # - Get follower count of each account.
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    is_correct = check_ansewer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False


