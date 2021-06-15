# This method plays a game of Mastermind with the user.

from random import *

def print_intro():
    print("Let's play Mastermind! Guess my four-digit number, and for")
    print("every guess you make, I'll tell you whether you have your")
    print("numbers in the right or wrong places, and how many of each!")

def code_is_correct(code_list, player_board):
    for i in range(len(code_list)):
        if code_list[i] != player_board[i]:
            return False
    return True

def play_game():
    secret_code = "5936"
    code_list = []
    for n in secret_code:
        code_list.append(n)
    print(code_list)
    player_board = [0] * len(code_list)
    while not code_is_correct(code_list, player_board):
        player_input = input("Type any 4-digit number: ")

        while not player_input.isdigit():
            print("Not a number. Try again.")
            player_input = input("Type any 4-digit number: ")

        while len(player_input) != 4:
            print("Not a 4-digit number. Try again.")
            player_input = input("Type any 4-digit number: ")

def main():
    print_intro()
    play_game()

main()