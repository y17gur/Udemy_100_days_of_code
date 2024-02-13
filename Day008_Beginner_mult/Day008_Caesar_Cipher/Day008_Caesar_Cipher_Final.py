# https://replit.com/@appbrewery/caesar-cipher-4-start

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(text_input, shift_num, direction_input):
    output_text = ""
    if direction_input == "decode":
        shift_num *= - 1
    for letter in text_input:
        if letter.isalpha():
            index = alphabet.index(letter)
            new_index = index + shift_num
            output_text += alphabet[new_index]
        else:
            output_text += letter
    print(f"The decoded text is {output_text}")


run_program = True

while run_program is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text_input=text, shift_num=shift, direction_input=direction)

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if answer == 'yes':
        run_program = True
    elif answer == 'no':
        print('Goodbye')
        run_program = False
    else:
        print("Wrong input!")
        run_program = False
