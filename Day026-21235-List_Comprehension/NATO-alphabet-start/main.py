import pandas

# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
frame = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
print([code_dict[letter] for letter in word if letter in code_dict.keys()])