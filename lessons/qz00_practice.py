"""Practice with if/else"""

__author__ = "730404552"

num: int = int(input("Choose a number between 0-100: "))

if num < 50:
    if num < 25:
        print("A")
    else:
        print("B")
else:
    if num > 75:
        print("C")
    else:
        print("D")