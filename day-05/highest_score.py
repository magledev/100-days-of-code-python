# Simple program to find the highest score within a list.

# Assign input variables.
student_scores = [int(x) for x in input(
    "Enter a list of student scores: ").split()]
print(student_scores)

highest_score = 0

# Iterate through student_score and compare with the next number to find the highest.
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest student score is: {highest_score}")
