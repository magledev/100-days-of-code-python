# Program to simulate the game Hangman

import random
from hangman_ascii import hangmen
from hangman_ascii import logo
from hangman_words import words


hangmen.reverse()

chosen_word = random.choice(words)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# print(f"\nThe hidden word is {chosen_word}")

print(logo)

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input(f"\nEnter a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(
            f"You've guessed {guess}, that's not in the hidden word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You've won!")

    print(hangmen[lives])
