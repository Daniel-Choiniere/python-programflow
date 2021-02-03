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

print("Aren't you glad you got out of there!")

