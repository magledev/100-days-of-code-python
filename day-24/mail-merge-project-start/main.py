NAME_PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()

print(names_list)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(NAME_PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as new_letter_file:
            new_letter_file.write(new_letter)
        print(new_letter)

