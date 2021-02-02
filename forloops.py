# parrot = "Norwegian Blue"
#
# for char in parrot:
#     print(char)

# number = "9,223:373:036 854,775:807"
number = input("Please enter a series of numbers, using any separators you like: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators += char

print(seperators)