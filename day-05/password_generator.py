# Simple program to act as a password generator.

import random

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", '"', "£", "$", "%", "^", "&", "*", "(", ")"]

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []

for x in range(0, nr_letters + 1):
    password_list += random.choice(letters)

for x in range(0, nr_numbers + 1):
    password_list += random.choice(numbers)

for x in range(0, nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print(f"Your randomly generated password is: {password}")
