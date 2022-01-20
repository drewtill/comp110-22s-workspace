"""An example of conditional (if-else) statements."""

SECRET: int = 3
SECRET2: int = 7

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly! :)")
    guess2: int = int(input("Guess another number between 1-10? "))
    if guess2 == SECRET2:
        print("You guessed correctly again!!")
        print("You have mastered the game.")
    else:
        print("You guessed the wrong number!")
        if guess2 > SECRET2:
            print("Your guess was too high!")
        else:
            print("Your guess was too low!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed to high.")
    else:
        print("You guessed too low.")
    print("Try running the program again!")

print("Game over.")