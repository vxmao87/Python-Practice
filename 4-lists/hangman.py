# This program plays a game of Hangman with the user.

def print_intro():
    print("Welcome to Hangman! Guess the word by guessing the letters")
    print("that make up the word, but you only have a limitied number")
    print("of times to guess, so be careful!")

def word_is_complete(board):
    for i in range(len(board)):
        if board[i] == "_":
            return False
    return True

def play_game():
    word = "exhilarating"
    word_list = []
    for c in word:
        word_list.append(c)
    print(word_list)
    player_board = ["_"] * (len(word_list))
    lives = len(word_list)
    while not word_is_complete(player_board):
        player_input = input("Type any letter from A to Z: ")


def main():
    print_intro()
    play_game()

main()