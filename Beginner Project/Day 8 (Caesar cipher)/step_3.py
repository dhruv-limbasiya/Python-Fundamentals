alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_word = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            cipher_word += letter
        else:
            shifted_postion = alphabets.index(letter) + shift_amount
            shifted_postion = shifted_postion % len(alphabets)
            cipher_word += alphabets[shifted_postion]
    print(f"here is the {encode_or_decode}d result: {cipher_word}")



should_continue = True

while should_continue == True:
    direction = input("type 'encode' for Encrypt, type 'decode' for decrypt: ").lower()
    word = input("Enter your message: ").lower().strip()
    shift = int(input("Enter Shift amount: "))

    caesar(word, shift, direction)

    restart = input("Type 'Yes' if you want to go again. Otherwise, type 'no': ").lower()
    if restart == "no":
        should_continue=False
        print("Good Bye")
