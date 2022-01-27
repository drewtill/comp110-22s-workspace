"""A wordle program that gives the user one oppotunity to guess."""

__author__ = "730404552"

# Set up variables for secret word and to get users input
secret_word: str = str("python")
user_guess: str = input(f"What is your { len(secret_word) }-letter guess? ") 
length_secret_word: int = int(len(secret_word))
# use an f-string to insert the length of the secret word into the sentence


# Here is the supplied code to implement the box characters from the COMP website
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# Use while statement to evaluate whether the user has inputed a 6 character word
# The loop makes the program repeat this function until the user has inputed a 6 character word
while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not { len(secret_word) } letters! Try again: ") 
# use an f-string to insert the length of the secret word into the sentence

# variables used to check for correct characters and to organize emojis
i: int = 0
box_color: str = str()


# variables used to keep track of correct characters that are in the wrong place
match_wrong_location: bool = False
alt_i: int = 0

# main while loop to check  all the conditions
while i < len(secret_word):
    # if statement to determine if character is correct
    if secret_word[i] == user_guess[i]:
        box_color = str(box_color) + str(GREEN_BOX) + " "
    # else statement begins test to determine if character is found somewhere else or not at all
    else:
        # have to reset variables for each character position
        match_wrong_location = False
        alt_i = 0
        # while statement checks the current character from user guess indicated by index i against all the characters in secret_word indicated by alt_i. 
        while not match_wrong_location and alt_i < len(secret_word):
            # if statement determines if found or no
            # then block will set bool to True if there is a match, leads to yellow box being printed
            if secret_word[alt_i] == user_guess[i]:
                match_wrong_location = True
            # else block will keep bool False and increase alt_i by one to check next location
            else:
                match_wrong_location = False
                alt_i += 1
        # finally the if else puts in the yellow or white box depending on if the bool is True or False.
        if match_wrong_location:
            box_color = str(box_color) + str(YELLOW_BOX) + " "
        else:
            box_color = str(box_color) + str(WHITE_BOX) + " "
    i += 1
            
# this prints out the str that is the emojis
print(box_color)

# Use an if else statement to determine if user has inputed the correct word
if secret_word == user_guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
