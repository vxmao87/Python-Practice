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
    guesses = 0

    while not code_is_correct(code_list, player_board):
        player_input = input("Type any 4-digit number: ")

        while not player_input.isdigit():
            print("Not a number. Try again.")
            player_input = input("Type any 4-digit number: ")

        while len(player_input) != 4:
            print("Not a 4-digit number. Try again.")
            player_input = input("Type any 4-digit number: ")

        for i in range(len(player_board)):
            player_board[i] = player_input[i]

        rnum_rplace = 0
        rnum_wplace = 0
        right_nums = [0] * len(player_board)
        for i in range(len(code_list)):
            if code_list[i] == player_board[i]:
                rnum_rplace += 1
                right_nums[i] = 1

        print(right_nums)
        if rnum_rplace != 4:
            wrong_nums = [0] * len(player_board)
            for i in range(len(player_board)):
                for j in range(len(player_board)):
                    if right_nums[i] != 1 and wrong_nums[j] != 2 and right_nums[j] != 1 and player_board[i] == code_list[j]:
                        rnum_wplace += 1
                        wrong_nums[j] = 2
            print("You have {} correct number(s) in the right place, and {} correct number(s) in the wrong place.".format(rnum_rplace, rnum_wplace))
            print(right_nums)
            print(wrong_nums)
        guesses += 1

    print("You win! You guessed my number {} in {} guess(es)!".format(secret_code, guesses))

def main():
    print_intro()
    play_game()

main()