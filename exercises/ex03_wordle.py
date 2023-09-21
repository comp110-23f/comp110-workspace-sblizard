"""Full Wordle Game."""

__author__ = "730642587"
word_to_guess: str = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(expected_len: int) -> str:
    """Makes sure the input is the correct number of characters long."""
    local_guess = input(f"Enter a {len(word_to_guess)} character word: ")
    while len(local_guess) != len(word_to_guess):
        local_guess = input(f"That wasn't {str(len(word_to_guess))} chars! Try again: ")
    return local_guess


def contains_char(search_in_word: str, char: str) -> bool:
    """Iterates through each character in search_in_word and returns True of char exists inside, else returns False."""
    assert len(char) == 1
    i = 0
    while i < len(search_in_word):
        if search_in_word[i] == char:
            return True
        i += 1
    return False


def emojified(guess_word: str, secret_answer: str) -> str:
    """Turns word into emoji."""
    assert len(guess_word) == len(secret_answer)
    emoji_string: str = ""
    i = 0
    while i < len(guess_word):
        if guess_word[i] == secret_answer[i]:
            emoji_string += GREEN_BOX
        elif contains_char(secret_answer, guess_word[i]):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        i += 1  
    return emoji_string


def main() -> None:
    """The entrypoint of the program and main game loop."""
    number_of_guesses: int = 0
    win_game: bool = False
    while (number_of_guesses <= len(word_to_guess)) and not (win_game):
        number_of_guesses += 1
        print(f"== Turn {number_of_guesses}/6 ==")
        
        guess = input_guess(len(word_to_guess))
        
        print(emojified(guess, word_to_guess))
        if emojified(guess, word_to_guess) == "\U0001F7E9" * int(len(word_to_guess)):
            win_game = True
    if win_game:
        print(f"You won in {number_of_guesses}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()