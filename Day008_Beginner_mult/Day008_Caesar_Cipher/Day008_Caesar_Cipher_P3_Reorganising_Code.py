# https://replit.com/@appbrewery/caesar-cipher-3-start

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#             ]


# def caesar(text_input, shift_num, direction_input):
#     new_letter = ""
#     output_text = ""
#     for letter in text_input:
#         if direction_input == "encode":
#             new_index = alphabet.index(letter) + shift_num
#             if new_index >= len(alphabet):
#                 new_index -= len(alphabet)
#                 new_letter = alphabet[new_index]
#             else:
#                 new_letter = alphabet[new_index]
#         elif direction_input == "decode":
#             new_index = alphabet.index(letter) - shift_num
#             if new_index < 0:
#                 new_index += len(alphabet)
#                 new_letter = alphabet[new_index]
#             else:
#                 new_letter = alphabet[new_index]
#         output_text += new_letter
#     print(f"The decoded text is {output_text}")


# def caesar(text_input, shift_num, direction_input):
#     new_letter = ""
#     output_text = ""
#     if direction_input == "decode":
#         shift_num *= - 1
#     for letter in text_input:
#         new_index = alphabet.index(letter) + shift_num
#         if new_index >= len(alphabet):
#             new_index -= len(alphabet)
#             new_letter = alphabet[new_index]
#         elif new_index < 0:
#             new_index += len(alphabet)
#             new_letter = alphabet[new_index]
#         output_text += new_letter
#     print(f"The decoded text is {output_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_input, shift_num, direction_input):
    output_text = ""
    if direction_input == "decode":
        shift_num *= - 1
    for letter in text_input:
        index = alphabet.index(letter)
        new_index = index + shift_num
        output_text += alphabet[new_index]
    print(f"The decoded text is {output_text}")


caesar(text_input=text, shift_num=shift, direction_input=direction)


# teacher
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         position = alphabet.index(char)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"Here's the {cipher_direction}d result: {end_text}")
#
#
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
