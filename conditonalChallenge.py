name = input("What is your name? ")
age = int(input("What is your age? "))

# if age >= 18 and age < 31:
if 18 <= age < 31:
    print("Welcome {} to the adults only holiday!".format(name))
else:
    print("I'm sorry {} you can not come on the Holiday".format(name))
