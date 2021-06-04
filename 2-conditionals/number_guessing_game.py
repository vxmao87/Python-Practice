# This method plays a variation of the number-guessign game with the user.
# The user will guess a number between 1 and 100, and the program will
# tell the user whether their guess is higher or lower than the number.

import random

# Prints an introductory message on how to play the game
def print_intro():
    print("Guess my number within the given interval, and I'll tell you")
    print("whether your number is higher or lower than my number!")
    print()

# Determines whether the number is higher or lower than the user's guess
def determine_distance(number, guess):
    if number > guess:
        return "higher"
    else:
        return "lower"

def main():
    number = random.randint(1, 100)
    guess = int(input("Guess my number! "))
    num_guesses = 1
    while guess != number:
        distance = determine_distance(number, guess)
        print("Incorrect. The correct number is", distance, "than your guess.")
        guess = int(input("Guess my number again! "))
        num_guesses += 1
    print("Nice! You guessed my number in", num_guesses, "tries.")

main()