import pandas as pd

ask_for_word = True

while ask_for_word:
    try:
        data_frame = pd.read_csv("nato_alphabet.csv")
        data_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

        word = input("Enter the word: ").upper()

        output = [data_dict[letter] for letter in word]



    except FileNotFoundError:
        with open("nato_alphabet.csv","a") as file:
            file.write("letter,code")
            file.write("\nA,Alfa")
            file.write("\nB,Bravo")
            file.write("\nC,Charlie")
            file.write("\nD,Delta")
            file.write("\nE,Echo")
            file.write("\nF,Foxtrot")
            file.write("\nG,Golf")
            file.write("\nH,Hotel")
            file.write("\nI,India")
            file.write("\nJ,Juliet")
            file.write("\nK,Kilo")
            file.write("\nL,Lima")
            file.write("\nM,Mike")
            file.write("\nN,November")
            file.write("\nP,Papa")
            file.write("\nO,Oscar")
            file.write("\nQ,Quebec")
            file.write("\nR,Romeo")
            file.write("\nS,Sierra")
            file.write("\nT,Tango")
            file.write("\nU,Uniform")
            file.write("\nV,Victor")
            file.write("\nW,Whiskey")
            file.write("\nX,X-ray")
            file.write("\nY,Yankee")
            file.write("\nZ,Zulu")

    except KeyError as keyerror:
        print(f"Sorry, only letters in the alphabet please. {keyerror} not valid.")

    else:
        print(output)
        ask_for_word = False