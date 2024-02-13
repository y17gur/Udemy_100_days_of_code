# https://replit.com/@appbrewery/caesar-cipher-2-start#main.py

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_num):
    cipher_text = ""
    for letter in plain_text:
        new_index = alphabet.index(letter) + shift_num
        if new_index >= len(alphabet):
            new_index -= len(alphabet)
            new_letter = alphabet[new_index]
        else:
            new_letter = alphabet[new_index]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#  Then call the correct function based on that 'drection' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.


def decrypt(cipher_text, shift_num):
    plain_text = ""
    for letter in cipher_text:
        new_index = alphabet.index(letter) - shift_num
        if new_index < 0:
            new_index += len(alphabet)
            new_letter = alphabet[new_index]
        else:
            new_letter = alphabet[new_index]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")


if direction == 'encode':
    encrypt(plain_text=text, shift_num=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_num=shift)


