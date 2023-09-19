"""One shot wordle!!!"""

__author__ = "730642587"

word_to_guess: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# input for user
guess = input(f"What is your {len(word_to_guess)}-letter guess? ")

# keeps making the user input until the lenght of the guess matches the length of the word to guess
while len(guess) != 6:
    guess = input(f"That was not {len(word_to_guess)} letters! Try again: ")

# initalizes variables to help with iteration and see if the answer is correct
index = 0
current_index_emoji = ""
correct = True

# iterate through each index of guess and compares to coresponding index of word_to_guess
while index < len(word_to_guess):
    if word_to_guess[index] == guess[index]:
        current_index_emoji = GREEN_BOX
    else:
        current_index_emoji = WHITE_BOX
        correct = False

    # determines if the current index of guess exists somewhere else in word_to_guess that isnt the same index
    exist_elsewhere = False
    i = 0
    while i < len(word_to_guess):
        if (guess[index] == word_to_guess[i]) and (i != index):
            exist_elsewhere = True
        i += 1

    if exist_elsewhere:
        current_index_emoji = YELLOW_BOX

    # prints out the correct emoji
    if index == len(word_to_guess) - 1:
        print(f"{current_index_emoji}")
    else:
        print(f"{current_index_emoji}", end="")
    index += 1

if correct:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")