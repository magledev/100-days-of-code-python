import os

# # Read
# with open("file.txt") as file:
#     file_contents = file.read()
#     print(file_contents)

filename = os.path.expanduser("../../../../Desktop/file.txt")

# Write
with open(filename, mode="a") as file:
    file.write("\nAnother random line of text")

with open(filename, mode="r") as file:
    print(file.read())
