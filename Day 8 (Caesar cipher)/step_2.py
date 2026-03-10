alphabats = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    cipher_word = ""
    for letter in original_text:
        shifted_postion = alphabats.index(letter) + shift_amount
        shifted_postion = shifted_postion % len(alphabats)
        cipher_word += alphabats[shifted_postion]
    print(f"Encrrpted word is: {cipher_word}")


def decrypt(original_text, shift_amount):
    decrypt_word = ""
    for letter in original_text:
        backword = alphabats.index(letter) - shift_amount
        backword = backword % len(alphabats)
        decrypt_word += alphabats[backword]
    print(f"Decrypt word is: {decrypt_word}")


word = input("Enter the word to decrypt: ")
shift = int(input("Enter Shift amount: "))

decrypt(word, shift)
