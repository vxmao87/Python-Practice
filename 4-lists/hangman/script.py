# This program plays a game of Hangman with the user.

import string
from random import *

player_score = 0

# Prints the introduction to the program
def print_intro():
    print("Welcome to Hangman! Guess the word by guessing the letters")
    print("that make up the word, but you only have a limitied number")
    print("of times to guess, so be careful!")

# Retrieves the player's inputted letter from the alphabet list by 
# returning the letter after it has been removed - code breaks once
# the letter is found
def grab_letter(alphabet_list, player_input):
    letter = ""
    for i in range(len(alphabet_list)):
        if alphabet_list[i] == player_input:
            letter = alphabet_list.pop(i)
            break
    return letter

# Prints the set of letters that the player has already guessed
# (or blanks if the letters have not been guessed yet)
def print_board(board):
    for i in range(len(board)):
        print(board[i], end = "")
    print()

# Checks the letter board for any remaining blanks - if there are none,
# the player has guessed the whole word completely
def word_is_complete(board):
    for i in range(len(board)):
        if board[i] == "_":
            return False
    return True

# Prints the number of lives the player has left
def evaluate_lives(lives):
    if lives == 1:
        print("You have 1 life remaining.")
    else:
        print("You have {} lives remaining.".format(lives))

# Depending on the number of lives, prints a message accordingly
def won_game(word, lives):
    if lives == 0:
        print("Sorry, you lose! The word was: {}.".format(word))
        return False
    else:
        print("You win!")
        print("You ended the game with {} lives. Congratulations!".format(lives))
        return True

# Asks the player if they want to play the game again
def play_again():
    answer = input("Would you like th play again? Type (y/n): ").lower()
    while answer not in ("y", "n"):
        print("Ivalid input. Try again!")
        answer = input("Would you like th play again? Type (y/n): ").lower()
    return answer == "y"

def choose_word(filename):
    dictionary = []
    with open(filename) as file:
        for line in file:
            dictionary.append(line)
    return choice(dictionary)

# Play a game of Hangman!
def play_game():

    # Creates a list of letters of the alphabet
    alphabet_list = list(string.ascii_lowercase)

    # The word the user has to guess
    word = choose_word("4-lists/hangman/dict.txt")

    # Breaks up the word into characters and stores each into a list
    word_list = []
    for c in word:
        word_list.append(c)

    # This is the player's board, or the word replaced with blanks.
    # It will fill up with the letters that the player guesses correctly.
    player_board = ["_"] * (len(word_list) - 1)

    # Number of lives in the game
    lives = 6

    # Set the player score as a global variable for use around the code
    global player_score

    # The game plays until the whole word is guessed
    # or the player runs out of lives
    while not word_is_complete(player_board) and lives != 0:
        print_board(player_board)
        player_input = input("Type any letter from A to Z: ")

        # If the input is not something in the alphabet list, 
        # the player is prompted again for a valid input.
        while player_input not in alphabet_list:
            print("Letter has already been used or value is invalid! Try again.")
            player_input = input("Type another letter from A to Z: ")

        # Obtains the letter from the alphabet list - the user input is
        # guaranteed to match with something inside the alphabet list
        # because of the above 'while' method - the letter is removed
        # from the alphabet list to prevent it from being used again
        letter = grab_letter(alphabet_list, player_input)

        # If the letter is not in the word, the player loses one life - 
        # otherwise, the blanks inside player_board will be filled with
        # the letter the user has inputted
        if letter not in word_list:
            lives -= 1
            print("Your letter is not in the word!")
        else:
            print("Your letter is in the word!")
            for i in range(len(word_list)):
                if word_list[i] == letter:
                    player_board[i] = letter

        # Evaluate the number of lives after every guess
        evaluate_lives(lives)

    # Ends the game and adds points if player wins the game
    if won_game(word, lives):
        player_score += 1

# Main method
def main():
    print_intro()
    play_game()

    # Run the game again if the player wishes to do so
    while play_again():
        play_game()

    # Prints the final score
    global player_score
    print("Your score is: {}".format(player_score))

main()