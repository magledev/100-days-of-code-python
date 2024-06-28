# Simple program to randomly select a bill paying.

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names as a comma separated list: ")
names = namesAsCSV.split(", ")

bill_payer = random.choice(names)

print(bill_payer)
