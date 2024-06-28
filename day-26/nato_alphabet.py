import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_df.to_dict()

nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

print(nato_alphabet)

phrase_letters = input(
    "Enter a word or phrase to convert using the phonetic alphabet: "
).upper()
print(phrase_letters)
phonetic_code = [nato_alphabet[letter] for letter in phrase_letters.replace(" ", "")]
print(phonetic_code)
