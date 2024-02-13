# https://replit.com/@appbrewery/caesar-cipher-4-start
# TODO-1: Import and print the logo from art.py when the program starts.
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
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if letter.isalpha():
            index = alphabet.index(letter)
            new_index = index + shift_num
            output_text += alphabet[new_index]
        else:
            output_text += letter
    print(f"The decoded text is {output_text}")


# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
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
