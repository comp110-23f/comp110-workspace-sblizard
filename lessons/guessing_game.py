"""program that loops until correct number is guessed."""

from random import randint

secret: int = randint(1,10)

guess: int = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    if guess < secret:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess a number between 1 and 10: "))

print(f"You got it! The correct number was {secret}.")