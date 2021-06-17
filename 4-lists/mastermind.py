# This method plays a game of Mastermind with the user. You can set the
# lengt of the code to be more than 4 digits, which is the default.

import random

# The length of the secret code to guess
code_length = 4

# Prints the introduction to the game
def print_intro():
    print("Let's play Mastermind! Guess my {}-digit number, and for".format(code_length))
    print("every guess you make, I'll tell you whether you have your")
    print("numbers in the right or wrong places, and how many of each!")

# If the player's input matches the generated code, return True
def code_is_correct(code_list, player_board):
    for i in range(len(code_list)):
        if code_list[i] != player_board[i]:
            return False
    return True

# Generates a random n-digit number, where n is the code length
def create_code():
    code = ""
    global code_length
    for i in range(code_length):
        code += str(random.randint(0, 9))
    return code

# Play Mastermind!
def play_game():

    # Create the code, and then store each number into a list
    secret_code = create_code()
    code_list = []
    for n in secret_code:
        code_list.append(n)

    # The player board that holds the user's inputted numbers
    player_board = [0] * len(code_list)

    # Number of guesses made
    guesses = 0

    # Make the code length a global variable
    global code_length

    # Keep asking for user guesses while the guesses do not match the secret code
    while not code_is_correct(code_list, player_board):
        player_input = input("Type any {}-digit number: ".format(code_length))

        # The input must be an integer
        while not player_input.isdigit():
            print("Not a number. Try again.")
            player_input = input("Type any {}-digit number: ".format(code_length))

        # The input must also be of length n, where n is the code length
        while len(player_input) != code_length:
            print("Not a {}-digit number. Try again.".format(code_length))
            player_input = input("Type any {}-digit number: ".format(code_length))

        # Stores each integer from the player's input into a list
        for i in range(len(player_board)):
            player_board[i] = player_input[i]

        # Counter for correct numbers in the RIGHT place
        rnum_rplace = 0

        # Counter for correct numbers in the WRONG place
        rnum_wplace = 0

        # Counter for keeping track of numbers gone through the below loops
        right_nums = [0] * len(player_board)

        # Mark each correct number in the right place with 
        # a 1 inside right_nums for future reference
        for i in range(len(code_list)):
            if code_list[i] == player_board[i]:
                rnum_rplace += 1
                right_nums[i] = 1

        # This method marks each correct number in the wrong place with a 2 inside
        # right_nums. If right_nums has a 1 on its slot, then the number doesn't
        # need to be looked at again by this loop, because it represents a correct
        # number in the right place. For the first instance that a number is found
        # that is in the wrong place, it is marked with a 2 and the rest of the loop
        # breaks via the done_looking boolean variable.
        #
        # Note that this method runs only if not every player-inputted number is correct
        # and in the right place.
        if rnum_rplace != code_length:
            for i in range(len(player_board)):
                done_looking = False
                for j in range(len(player_board)):
                    if not done_looking and right_nums[j] != 1 and right_nums[j] != 2 and player_board[i] == code_list[j]:
                        rnum_wplace += 1
                        right_nums[j] = 2
                        done_looking = True
            print("You have {} correct number(s) in the right place, and {} correct number(s) in the wrong place.".format(rnum_rplace, rnum_wplace))

        # No matter the outcome, one guess is added
        guesses += 1

    # Prints the winning message
    print("You win! You guessed my number {} in {} guess(es)!".format(secret_code, guesses))

# Main method
def main():
    print_intro()
    play_game()

main()