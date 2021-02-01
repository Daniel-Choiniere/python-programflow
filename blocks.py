# for i in range(1, 13):
#     print("No. {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0} ".format(name)))
print("{0} is {1} years old.".format(name, age))

if age >= 18:
    print("I am legal age to vote!")
    print("Please put X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
else:
    print("I am legal age to vote!")
    print("Please put X in the box")
