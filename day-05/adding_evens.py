# Simple program to calculate to sum of all even numbers in a range.
total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# Different method.
total2 = 0

for number in range(0, 101, 2):
    total2 += number
print(total2)
