import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in nato_alphabet_df.iterrows()}
print(nato_alphabet)

def generate_phonetic_code():
    phrase_letters = input("Enter a word or phrase to convert using the phonetic alphabet: ").upper()
    try:
        phonetic_code = [nato_alphabet[letter] for letter in phrase_letters.replace(" ", "")]
    except KeyError:
        print("You can only enter letters of the alphabet")
        generate_phonetic_code()
    else:
        print(phonetic_code)

generate_phonetic_code()
