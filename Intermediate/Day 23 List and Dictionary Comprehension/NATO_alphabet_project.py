import pandas as pd

# 1. we read the csv file
data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

# 2. we iterate row with help to iterrows() and we assign letter as key, code and value of data_dict dictionary
data_dict = {row.letter : row.code for (index,row) in data_frame.iterrows()}

# 3. take input from user and convert it in uppercase
word = input("Enter a Word: ").upper()

# 4. when we itrate word it start from 0 to n so we itrate word and each letter find in data_dict and append in output
output = [data_dict[letter] for letter in word]

print(output)