answer= 5

print("Please guess a number between 1 and 10: ")
# Need to convert the input to an integer because it is default a str
guess = int(input())

if guess < answer:
    print("Please guess a higher number")
elif guess > answer:
    print("Please guess a lower number")
else:
    print("You guessed the number right!")