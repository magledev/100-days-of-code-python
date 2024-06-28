# Simple program to calculate remaining life expectancy, based on living until life_span years old.

# Set input variables
age = int(input("What is your current age? "))
life_span = int(input("What is your life expectancy? "))

# Calculate working variables
x = (life_span - age) * 365
y = (life_span - age) * 52
z = (life_span - age) * 12

# Output statement
print(f"You have {x} days, {y} weeks and {z} months remaining")
