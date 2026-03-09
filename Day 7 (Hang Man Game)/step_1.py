import random

word_list = ["jaguar", "lion", "wolf"]

chosen_word = random.choice(word_list)

print(chosen_word)

guess_letter = input("Guess a Letter: ").lower()

for letter in chosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")