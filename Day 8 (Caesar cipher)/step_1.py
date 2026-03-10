alphabats=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_word=""
    for letter in original_text:
        shifted_postion = alphabats.index(letter)+shift_amount
        shifted_postion = shifted_postion % len(alphabats)
        cipher_word += alphabats[shifted_postion]
    print(f"Encrypted word is: {cipher_word}")

word=input("Enter the word to encrypt: ")
shift=int(input("Enter Shift amount: "))

encrypt(word, shift)


# alphabats=[]
#
# for letter in range(ord("a"), ord("z")+1):
#     alphabats.append(chr(letter))
#
# print(alphabats)