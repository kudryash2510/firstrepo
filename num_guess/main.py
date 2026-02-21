import random

game = random.randint(1, 100)

guess = int(input("Guess number 1-100: "))

while guess != game:
    if guess > game:
        print("Incorrect, the number should be less!")
    elif guess < game:
        print("Incorrect, the number should be higher!")
    guess = int(input("Guess number 1-100: "))
print("You're right!")