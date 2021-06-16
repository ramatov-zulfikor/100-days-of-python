import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

user_word = input("Enter a word:\n").upper()
result = [alphabet_dict[letter] for letter in user_word]
print(result)
