"""A step towards wordle """

__author__ = "730642587"

guess_word = input("Enter a 5-character word: ")

if len(guess_word) != 5:
    print("Error: word must be 5 characters long")
    exit()

guessed_character = input("Enter a single character: ")

if  len(guessed_character) != 1:
    print("Error: character must be a single character")
    exit()
    
    
print("Searching for " + guessed_character + " in " + guess_word)

char_count: int = 0

for i in range(5):
    if guess_word[i]==guessed_character:
        char_count+=1
        print(guessed_character + " found at index " + str((i)))

if char_count == 0:
    print("No instances of " + guessed_character + " found in " + guess_word)
else:
    print(str(char_count) + " instances of " + guessed_character + " found in " + guess_word)

