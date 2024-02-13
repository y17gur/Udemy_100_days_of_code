import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

dictionary = {row.letter: row.code for (index, row) in alphabet.iterrows()}
# print(dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input('Input the word: ').upper()
#
# # out_list = [row.code for (index, row) in alphabet.iterrows() if row.letter in word]
# # print(out_list)
#
# out_list = [dictionary[letter] for letter in word]
# print(out_list)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
