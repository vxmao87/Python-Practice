# This method plays a variation of the number-guessign game with the user.
# The user will pick a number between 1 and 100, and the program will
# try to guess the user's number. The user can tell the program whether
# its number is higher or lower that the user's actual number.

import random

def print_intro():
    print("Think of any number between 1 and 100, and you can tell me")
    print("whether my guess is higher or lower than your number!")

def play_game():

    # Set the bounds of the numbers to guess from 1 to 100
    high_bound = 100
    low_bound = 1

    # Program makes the guess using the bounds above
    guess = random.randint(low_bound, high_bound)

    # Tracks the number of guesses made
    num_guesses = 1

    # Asks the user if the guess is higher or lower than their number
    answer = input("Is your number {}? Type (y/n): ".format(guess))

    # If the answer typed is NOT 'y' or 'n'
    while answer.lower() != 'y' and answer.lower() != 'n':
        print("Invalid input. Try again.")
        answer = input("Is your number {}? Type (y/n): ".format(guess))

    # If the answer typed is 'n'
    while answer.lower() != 'y':
        num_guesses += 1

        # Program asks user if its guess is higher or lower than the user's number
        hint = input("Is your number higher or lower? Type (h/l): ")

        # If neither 'h' or 'l' gets typed, an error message pops up
        while hint.lower() != 'h' and hint.lower() != 'l':
            print("Invalid input. Try again.")
            hint = input("Is your number higher or lower? Type (h/l): ")

        # Changes the bounds of the program's guess depending on the user input
        if hint.lower() == 'h':
            low_bound = guess + 1
        else:
            high_bound = guess - 1
        
        print("Bounds: {} to {}".format(low_bound, high_bound))

        # Makes another guess and asks the user again
        guess = random.randint(low_bound, high_bound)
        answer = input("Is your number {}? Type (y/n): ".format(guess))

    # Prints the user's number and the number of guesses the program made
    print("Nice! I got your number ({}) right in {} guesses.".format(guess, num_guesses))

def main():
    print_intro()
    ready = input("Type y when you are ready with your number: ")

    # If the user does NOT type 'y', an error message occurs
    while ready.lower() != "y":
        print("Invalid input. Try again.")
        ready = input("Type y when you are ready with your number: ")
    
    play_game()
    
main()