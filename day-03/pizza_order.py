# Program to calculate price of a pizza order.

# Print welcome message
print("Welcome to python pizza deliveries")

# Assign input variables
size = input("What size pizza do you require? S, M or L: ")
add_pepperoni = input("Do you require pepperoni? Y or N: ")
extra_cheese = input("Do you require extra cheese? Y or N: ")

bill = 0

# Calculate cost of base pizza
if size == "S" or size == "s":
    bill += 5
if size == "M" or size == "m":
    bill += 10
if size == "L" or size == "l":
    bill += 15

# Calculate cost of any toppings:
if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S":
        bill += 1
    else:
        bill += 2
if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

# Output final bill
print(f"You final bill is £{bill}")
