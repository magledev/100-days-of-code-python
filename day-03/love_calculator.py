# Simple program to calculate whether two people are compatible with each other, bases upon how many times the letters in their names occur in the words true love.

# Print welcome statement
print("Welcome to the Love Calculator")

# Assign input variables
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_string = (name1 + name2).lower()

letter_count1 = 0
letter_count2 = 0

letter_count1 += names_string.count("t")
letter_count1 += names_string.count("r")
letter_count1 += names_string.count("u")
letter_count1 += names_string.count("e")

letter_count2 += names_string.count("l")
letter_count2 += names_string.count("o")
letter_count2 += names_string.count("v")
letter_count2 += names_string.count("e")

love_word = int(f"{letter_count1}{letter_count2}")

if love_word <= 10 or love_word > 90:
    print(f"Your score is {love_word}, you go together like coke and mentos")
elif love_word >= 40 and love_word <= 50:
    print(f"Your score is {love_word}, you are alright together")
else:
    print(f"Your score is {love_word}")
