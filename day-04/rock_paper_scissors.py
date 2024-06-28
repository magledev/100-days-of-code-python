# Program to simulate the game Rock, Paper, Scissors.

import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Space Invader
invader = ("""
      ##      ##         
    ##############
  ####  ######  ####
######################
##  ##############  ##     
##  ##          ##  ##
      ####  #### 
""")

# Create list of moves to easily reference via indices
moves = [rock, paper, scissors]

# Set player moves from input variables
player_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

# Print chosen moves as ascii art
if player_choice < 0 or player_choice > 2:
    print(invader)
else:
    print(f"{moves[player_choice]}")
print(f"Computer chose:\n{moves[computer_choice]}")

# Logical analysis to determine a winner and output the result.
if player_choice >= 3 or player_choice < 0:
    print("The only valid inputs are 0, 1 or 2.\nYou lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("It's a draw!")

# if player_choice == 0 and computer_choice == 0:
#     print("Draw. Play again.")
# if player_choice == 1 and computer_choice == 1:
#     print("Draw. Play again.")
# if player_choice == 2 and computer_choice == 2:
#     print("Draw. Play again.")

# if player_choice == 0 and computer_choice == 1:
#     print("You lose.")
# if player_choice == 0 and computer_choice == 2:
#     print("You win.")

# if player_choice == 1 and computer_choice == 0:
#     print("You win.")
# if player_choice == 1 and computer_choice == 2:
#     print("You lose.")

# if player_choice == 2 and computer_choice == 0:
#     print("You lose.")
# if player_choice == 2 and computer_choice == 1:
#     print("You win.")
