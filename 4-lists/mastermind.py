# This method plays a game of Mastermind with the user.

from random import *

def print_intro():
    print("Let's play Mastermind! Guess my four-digit number, and for")
    print("every guess you make, I'll tell you whether you have your")
    print("numbers in the right or wrong places, and how many of each!")

def play_game():
    secret_code = "5936"
    code_list = []
    for n in secret_code:
        code_list.append(n)
    print(code_list)

def main():
    print_intro()
    play_game()

main()