# This method plays a variation of the number-guessign game with the user.
# The user will pick a number between 1 and 100, and the program will
# try to guess the user's number. The user can tell the program whether
# its number is higher or lower that the user's actual number.

import random

def print_intro():
    print("Think of any number between 1 and 100, and you can tell me")
    print("whether my guess is higher or lower than your number!")

def play_game():
    high_bound = 101
    low_bound = 1
    guess = random.randint(low_bound, high_bound)
    num_guesses = 1
    answer = input("Is your number {}? Type (y/n): ".format(guess))
    while answer.lower() != 'y' and answer.lower() != 'n':
        print("Invalid input. Try again.")
        answer = input("Is your number {}? Type (y/n): ".format(guess))
    while answer.lower() != 'y':
        num_guesses += 1
        hint = input("Is your number higher or lower? Type (h/l): ")
        while hint.lower() != 'h' and hint.lower() != 'l':
            print("Invalid input. Try again.")
            hint = input("Is your number higher or lower? Type (h/l): ")
        if hint.lower() == 'h':
            low_bound = guess
        else:
            high_bound = guess
        guess = random.randint(low_bound, high_bound)
        answer = input("Is your number {}? Type (y/n): ".format(guess))
    print("Nice! I got your number ({}) right in {} guesses.".format(guess, num_guesses))
    

def main():
    print_intro()
    ready = input("Type y when you are ready with your number: ")
    while ready.lower() != "y":
        print("Invalid input. Try again.")
        ready = input("Type y when you are ready with your number: ")
    play_game()
    
main()