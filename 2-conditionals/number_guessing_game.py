# This method plays the number-guessign game with the user.
# The user will guess a number between 1 and 100, and the program will
# tell the user whether their guess is higher or lower than the number.

import random

# Prints an introductory message on how to play the game
def print_intro():
    print("Guess my number within the given interval, and I'll tell you")
    print("whether your number is higher or lower than my number!")

# Determines whether the number is higher or lower than the user's guess
def determine_distance(number, guess):
    if number > guess:
        return "higher"
    else:
        return "lower"

def get_guess():
    guess = int(input("Guess my number! "))
    while guess < 0 or guess > 100:
        print("Out of range. Try again.")
        guess = int(input("Guess my number! "))
    return guess

def play_game():
    number = random.randint(1, 101)
    guess = get_guess()
    num_guesses = 1
    while guess != number:
        distance = determine_distance(number, guess)
        print("Incorrect. The correct number is", distance, "than your guess.")
        guess = get_guess()
        num_guesses += 1
    print("Nice! You guessed my number in", num_guesses, "tries.")
    return num_guesses

def main():
    print_intro()
    guess_total = play_game()
    games = 1
    play_again = input("Would you like to play again? (Type y/n)")
    while play_again.lower() != "n":
        guess_total += play_game()
        games += 1
        play_again = input("Would you like to play again? (Type y/n)")
    average = guess_total / games
    print("You made {} total guesses, played {} games, and took an average of {} guesses in a game.".format(guess_total, games, average))

main()