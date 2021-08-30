import pandas

# {new_key:new_value for (index, row) in df.iterrows()}

frame = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in frame.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    try:
        output = [code_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output)
        break
