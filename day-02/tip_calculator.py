# Simple program to calculate tip left on a bill, based on no_payers paying the bill.

# Print welcome message
print("Welcome to the tip calculator.")

# Set input variables
bill_total = float(input("What was the total bill? £"))
tip_value = int(input("What percentage tip would you like to give 10%, 12%, or 15%? "))
no_payers = int(input("How many people will split the bill? "))

# Output statement
print(
    f"Each person should pay: {round((bill_total * 1 + tip_value) / no_payers, 2):.2f }"
)
