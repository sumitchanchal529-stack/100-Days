import Caser_Cipher_Art

print(Caser_Cipher_Art.logo)

print("Welcome to Caesar Cipher")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shifted_amount, encode_or_decode):
    cipher_text = ""

    # If decoding, make the shift negative
    if encode_or_decode == "decode":
        shifted_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shifted_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    caesar(original_text=text, shifted_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")