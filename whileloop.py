# for i in range(10):
#     print("i is now {}".format(i))

# same thing using while loop
i = 0;
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

avaiable_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in avaiable_exits:
    chosen_exit = input("Please choose another direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Aren't you glad you got out of there!")

# challenges
# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

# Write a program to print out all numbers from 0 to 20 that are not divisible by 3 or 5
for i in range(1, 21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
