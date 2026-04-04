import pandas as pd

data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data_frame)

data_dict = {row.letter : row.code for (index, row) in data_frame.iterrows()}

print(data_dict)

word = input("Enter a Word: ").upper()

output = [data_dict[letter] for letter in word]
print(output)