import random

n = random.randint(1, 10)
guess = 0

while guess != n:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess > n:
        print("Too high!")
    elif guess < n:
        print("Too low!")
    else:
        print("You guessed it!")
