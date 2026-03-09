import random

word_list = ["jaguar", "lion", "wolf"]

chosen_word = random.choice(word_list)

for i in range(1, len(chosen_word) + 1):
    print("_", end="")

game_over = False

current_letter = []

while not game_over:
    guess_letter = input("\nGuess a Letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess_letter:
            display += letter
            current_letter.append(guess_letter)
        elif letter in current_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
