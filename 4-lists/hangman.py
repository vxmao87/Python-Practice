# This program plays a game of Hangman with the user.

import string

def print_intro():
    print("Welcome to Hangman! Guess the word by guessing the letters")
    print("that make up the word, but you only have a limitied number")
    print("of times to guess, so be careful!")

def grab_letter(alphabet_list, player_input):
    letter = ""
    for i in range(len(alphabet_list)):
        if alphabet_list[i] == player_input:
            letter = alphabet_list.pop(i)
            break
    return letter

def print_board(board):
    for i in range(len(board)):
        print(board[i], end = "")

def word_is_complete(board):
    for i in range(len(board)):
        if board[i] == "_":
            return False
    return True

def evaluate_lives(lives):
    if lives == 1:
        print("You have 1 life remaining.")
    else:
        print("You have {} lives remaining.".format(lives))

def end_game(word, lives):
    if lives == 0:
        print("Sorry, you lose! The word was: {}.".format(word))
    else:
        print("You win!")
        print("You ended the game with {} lives. Congratulations!".format(lives))

def play_game():
    alphabet_list = list(string.ascii_lowercase)
    word = "supercalifragilisticexpialidocious"
    word_list = []
    for c in word:
        word_list.append(c)
    player_board = ["_"] * (len(word_list))
    lives = 10
    while not word_is_complete(player_board) and lives != 0:
        print_board(player_board)
        player_input = input(" Type any letter from A to Z: ")
        while player_input not in alphabet_list:
            print("Letter has already been used or value is invalid! Try again.")
            player_input = input("Type another letter from A to Z: ")
        letter = grab_letter(alphabet_list, player_input)
        print(letter)
        if letter not in word_list:
            lives -= 1
        else:
            print("Your letter is in the word!")
            for i in range(len(word_list)):
                if word_list[i] == letter:
                    player_board[i] = letter
        evaluate_lives(lives)
    end_game(word, lives)

def main():
    print_intro()
    play_game()

main()