"""A step towards wordle """

__author__ = "730642587"

guessWord = input("Enter a 5-character word: ")

if len(guessWord) != 5:
    print("Error: word must be 5 characters long")
    exit()

guessedCharacter = input("Enter a single character: ")

if  len(guessedCharacter) != 1:
    print("Error: character must be a single character")
    exit()
    
    
print("Searching for " + guessedCharacter + " in " + guessWord)

charCount: int = 0

for i in range(5):
    if guessWord[i]==guessedCharacter:
        charCount+=1
        print(guessedCharacter + " found at index " + str((i)))

if charCount == 0:
    print("No instances of " + guessedCharacter + " found in " + guessWord)
else:
    print(str(charCount) + " instances of " + guessedCharacter + " found in " + guessWord)

