choices = ["1. Go Onewheeling", "2. Go Mountian Biking", "3. Take a shower",
           "4. Work on Python", "5. Watch a movie", "0. Exit"]

print(choices)

chosen = ""
while chosen != 0:
    chosen = int(input("Please choose an option number from the list of choices."))
    print("You have chosen to {}".format(choices[chosen - 1]))
else:
    print("Thanks for playing")