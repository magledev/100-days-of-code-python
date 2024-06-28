# Simple program to simulate a coin toss, i.e output heads or tails.

import random

# Generate a seed number from an int input
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_int = random.randint(0, 1)

print(random_int)

if random_int == 1:
    print("Heads")
else:
    print("Tails")
