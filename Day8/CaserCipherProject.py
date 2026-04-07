print("Welcome to Caser Cipher ")
alphabet = ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
direction = input("Type encode to encrypt and  type decode to decrypt ").lower()
text = input("type your message :").lower()
shift = int(input("Type the shift number :"))

def encryped(orignal_text, shifted_amount):
    cipher_text = ""
    for letter in orignal_text:
        shifted_position = alphabet.index(letter)+ shifted_amount
        shifted_position %= len(alphabet)
        cipher_text += shifted_position

    print(f"here is the encoded message:{cipher_text}")

print(encryped())
# def decrypted(orignal_text = text, shift_amount = shift):
