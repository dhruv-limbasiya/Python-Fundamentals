import random

word_list = ["jaguar", "lion", "wolf"]

chosen_word = random.choice(word_list)

for i in range(1, len(chosen_word) + 1):
    print("_", end="")

guess_letter = input("\nGuess a Letter: ").lower()

for letter in chosen_word:
    if letter == guess_letter:
        print(letter,end="")
    else:
        print("_",end="")