"""Files! Wee. Today is just about writing files in python, a thing I have done but don't do very often.
We can do it like this:
file = open("day_24/my_file.txt")
contents = file.read()
print(contents)
file.close() """
#Or like this:
# with open("day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# Or we can write:
# with open("day_24/my_file.txt", mode="w") as file:
#     file.write("new text!")
# Or we can append:
# with open("day_24/my_file.txt", mode="a") as file:
#     file.write("new text!")
# Or we can make new files:
# with open("day_24/new_file.txt", mode="w") as file:
#     file.write("new text in new file!")

# I already knew this, but hey, here's an absolute file path grabbing something from a desktop:
# FILE="C:/Users/youruser/Desktop/new_file.txt"
# with open(FILE) as file:
#     contents=file.read()
#     print(contents)

# and here's relative grabbing from a desktop (from where my code is running):
FILE="../../../Desktop/new_file.txt"
with open(FILE) as file:
    contents=file.read()
    print(contents)