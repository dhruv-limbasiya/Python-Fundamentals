import random

chance_for_hard = 5
chance_for_easy = 10

def check_answer(user_guess, actual_answer, truns):
    """checks answer against guess, returns the number of turns remining"""
    if user_guess >  actual_answer:
        print("Too high")
        return truns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return truns - 1
    elif user_guess == actual_answer:
        print(f"You get it! the answer was {actual_answer}")


def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return chance_for_easy
    else:
        return chance_for_hard


def game():
    print("Welcom to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    print(f"The answer is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()