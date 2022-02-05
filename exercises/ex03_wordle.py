"""A wordle game that allows the user to play until they get it right."""

__author__ = "730404552"


# contains_char measures to see if character found in word or not
def contains_char(guess: str, char: str) -> bool:
    """Function to determine if a character is found within a string."""
    assert len(char) == 1
    # set i = 0 to account for each char
    i: int = 0
    # use while loop to test whether the char is found in the word
    while len(guess) > i:
        if guess[i] == char:
            # if it is found in the word return True
            return True
        else:
            i += 1
    # if it is never found in the word return False
    return False


# setup variables to use for the colored box emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# use emojified to return a str of emojis
def emojified(user_guess: str, secret: str) -> str:
    """Will return string of emojis yellow or white based on contains_char."""
    assert len(user_guess) == len(secret)
    # use emoji_i to test at each char
    emoji_i: int = 0
    # setup a str var that can be returned at the end
    emoji_string: str = ""
    # a while loop to evaluate each char in the word
    while len(secret) > emoji_i:
        # the first if will determine if it is a direct match (green box)
        if user_guess[emoji_i] == secret[emoji_i]:
            emoji_string += GREEN_BOX
        else:
            # the second if returns a Yellow box if contains_char returns true. (This means the char was found at a location within the word)
            if contains_char(secret, user_guess[emoji_i]):
                emoji_string += YELLOW_BOX
            else:
                # finally if the char is nowhere to be found we add a White box to the str
                emoji_string += WHITE_BOX
        # must increment the counter var to work through the word
        emoji_i += 1
    # finish function by returning the resulting str
    return emoji_string


# use input_guess to gather the users input for their guess word
def input_guess(guess_length: int) -> str:
    """Gather the users guess."""
    user_guess: str = input(f"Enter a { guess_length } character word: ")
    while len(user_guess) != guess_length:
        user_guess = input(f"That was not { guess_length } chars! Try again: ")
    return user_guess


# finally, we get to bring it all together with the main function
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # create var turns to keep count of turns left for user
    turns: int = 1
    # create var secret_word to determine the secret str
    secret_word: str = "codes"
    # I used var correct_guess to stop the while loop when the user gets the right guess
    correct_guess: bool = False
    while turns <= 6 and not correct_guess:
        # print the turns left and functions to gather user input and provide feedback
        print(f"=== Turn { turns }/6 ===")
        guessed_word: str = input_guess(len(secret_word))
        print(emojified(guessed_word, secret_word))
        # if statement to test if user was right.
        # Sets correct_guess to True to indicate user has finished
        if secret_word == guessed_word:
            print(f"You won in { turns }/6 turns!")
            correct_guess = True
        # increase turns by one for each turn
        turns += 1
    # use this if statement to tell user the game is over if all 6 guesses fail
    if turns == 7 and not correct_guess:
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()