hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]
import random

word_list = ["jaguar", "lion", "wolf"]
chosen_word = random.choice(word_list)

print("_ " * len(chosen_word))

game_over = False
lives = 6
current_letter = []

while not game_over:
    guess_letter = input("\nGuess a Letter: ").lower()

    if guess_letter in current_letter:
        print("You already guessed that letter.")
        continue

    if guess_letter not in chosen_word:
        lives -= 1
        print("Wrong guess!")
        print(f"******** You Have {lives} Lives Left ********")

    display = ""

    for letter in chosen_word:
        if letter == guess_letter:
            display += letter
            if guess_letter not in current_letter:
                current_letter.append(guess_letter)
        elif letter in current_letter:
            display += letter
        else:
            display += "_"

    print(display)
    print(hangman_stages[5 - lives])

    if lives == 0:
        print("******** You Lose ********")
        print("Word Was:", chosen_word)
        game_over = True
    elif "_" not in display:
        print("******** You Win ********")
        game_over = True