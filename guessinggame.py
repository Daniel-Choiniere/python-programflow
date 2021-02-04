import random

highest_value = 10
answer = random.randint(1, highest_value)
print(answer) # only for testing purposes - REMOVE AFTER TESTING

print("Please guess a number between 1 and {}: ".format(highest_value))
# Need to convert the input to an integer because it is default a str
guess = int(input())

if guess == answer:
    print("You guessed right the first time!")

else:
    while guess != answer and guess != 0:
        if guess < answer:
            print("Please guess higher, or enter 0 to exit game")
        else:
            print("Please guess lower, or enter 0 to exit game")
        guess = int(input())
        if guess == answer:
            print("well done, you guessed it")
        else:
            if guess == 0:
                print("Exit game. Thanks for playing, try again sometime!")
            else:
                print("sorry, you have not guessed correctly")




