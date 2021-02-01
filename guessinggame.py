answer = 5

print("Please guess a number between 1 and 10: ")
# Need to convert the input to an integer because it is default a str
guess = int(input())

if guess == answer:
    print("You guessed right the first time!")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    quess = int(input())
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("sorry, you have not guessed correctly")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     quess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry, you have not guessed correctly")
# else:
#     print("You guessed right the first time!")


# if guess < answer:
#     print("Please guess a higher number")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you did not guess correctly")
# elif guess > answer:
#     print("Please guess a lower number")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you did not guess correctly")
# else:
#     print("You guessed the number right!")

