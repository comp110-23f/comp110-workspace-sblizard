"""One shot wordle!!!"""

__author__ = "730642587"

word_to_guess: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = input(f"What is your {len(word_to_guess)}-letter guess? ")

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")

index = 0

currentIndexEmoji = ""

correct = True

while index < len(word_to_guess):
    if word_to_guess[index] == guess[index]:
        currentIndexEmoji = GREEN_BOX
    elif guess[index] in word_to_guess:
        currentIndexEmoji = YELLOW_BOX
        correct = False
    else:
        currentIndexEmoji = WHITE_BOX
        correct = False
    if index == len(word_to_guess)-1:
        print(f"{currentIndexEmoji}")
    else:
        print(f"{currentIndexEmoji}", end="")
    index += 1

if correct:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")



