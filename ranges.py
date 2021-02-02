for i in range(1, 21):
    print("i is now {}".format(i))

print()

# using steps in range
for i in range(0, 10,2 ):
    print("i is now {}".format(i))

print()

# stepping in reverse
for i in range(10, 0, -2 ):
    print("i is now {}".format(i))


age = int(input("How old are you? "))

# using range instead fo conditional
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

# challenge - Write a program to print out all numbers from 0 -100 that are divisible by 7
for i in range(0, 101):
    if i % 7 == 0:
        print(i)