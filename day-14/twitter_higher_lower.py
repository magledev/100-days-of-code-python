# A game of higher/lower using follower count for various accounts on Twitter.

import random
import art
from game_data import data
import clear_screen

# Get random personality from game_data and display various info about them. Store in a dictionary called A.


def format_account(account):
    """Retrieve the Twitter account data and returns a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Print art.
print(art.logo)
score = 0
continue_game = True
# Get random account from game_data
account_b = random.choice(data)

# Make the game repeatable
while continue_game == True:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_account(account_b)}.")

    # Get guess from player
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds.
    clear_screen.clear()
    print(art.logo)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
