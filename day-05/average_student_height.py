# Simple program to calculate the average height of a student from a list of student heights.

# Set variables
student_heights = input("Input a list of student heights: ").split()
total_student_height = 0
number_of_students = 0

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

print(student_heights)

# Use for loop to iterate through list of student_heights, incrementing count each time.
for height in student_heights:
    total_student_height += int(height)
    number_of_students += 1

# Output statement with result.
print(
    f"The average height of a student is: {round(total_student_height / number_of_students )}cm")
