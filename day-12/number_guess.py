# A simple guess the number game

from random import randint
from art import logo

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5


# Function to check guess against secret_number.
def check_number(guess, secret_number, attempts):
    """Check secret_number against guess. Returns the number of attempts remaining."""
    if guess > secret_number:
        print(
            f"\nToo high.")
        return attempts - 1
    elif guess < secret_number:
        print(
            f"\nToo low.")
        return attempts - 1
    else:
        print(
            f"\nCorrect! You successfully guessed the secret number. You had {attempts} attempts remaining.")


# Function to set difficulty level. i.e number of lives.
def set_difficulty():
    difficulty = input("\nChoose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_LIVES
    elif difficulty == 'hard':
        return HARD_LEVEL_LIVES


# Main game function.
def game():
    print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    secret_number = randint(1, 100)
    attempts = set_difficulty()
    guess = 0

    while guess != secret_number and attempts > 0:
        print(
            f"\nYou have {attempts} attempts remaining to guess the secret number.")
        guess = int(input("\nMake a guess: "))
        attempts = check_number(guess, secret_number, attempts)
        if attempts == 0:
            print("\nYou have no more lives remaining. Games over!")
            return
        elif guess != secret_number:
            print("\nGuess again.")


game()
