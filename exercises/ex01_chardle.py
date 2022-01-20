"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730404552"


# Variables are named below. I also need to check for count of characters as soon as the input is recieved to keep the program from continuing if an exit is needed. 
# This is used for Part 1
word: str = input("Enter a 5-character word: ")
# Here I have the program check to see if the word is more or less than 5 characters (Part 4)
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
# Here I have the program check to see if there is only one character (Part 4)
if len(character) < 1:
    print("Error: Character must be a single character.")
    exit()
if len(character) > 1:
    print("Error: Character must be a single character.")
    exit()

# I set match_count variable equal to zero and then add one for each character match (Part 3)
match_count: int = 0


# Here I have program say that it is searching for the character in the word
# Also used for Part 1
print("Searching for " + character + " in " + word)

# I used if statements to determine if the character was found in the word at each index (Part 2)

if word[0] == character:
    print(character + " found at index 0")
    match_count = match_count + 1

if word[1] == character:
    print(character + " found at index 1")
    match_count = match_count + 1

if word[2] == character:
    print(character + " found at index 2")
    match_count = match_count + 1

if word[3] == character:
    print(character + " found at index 3")
    match_count = match_count + 1

if word[4] == character:
    print(character + " found at index 4")
    match_count = match_count + 1


# I setup an if else function to determine if the character is found in the word or not.
# If the character is not found it states no instances of character found in word
# Other wise it starts another if/else statement to provide the proper pluralization of the word instance/s. Accomplish this by determining if match count equals 1, otherwise will be above one because we removed the less than one possibily with the first if/else statement
# Used for part 3
if match_count < 1:
    print("No instances of " + character + " found in " + word)
else:
    if match_count == 1:
        print(match_count, "instance of " + character + " found in " + word)
    else:
        print(match_count, "instances of " + character + " found in " + word)