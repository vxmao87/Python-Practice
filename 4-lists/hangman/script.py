# This program plays a game of Hangman with the user.

import random

player_score = 0

# Prints the introduction to the program
def print_intro():
    print("Welcome to Hangman! Guess the word by guessing the letters")
    print("that make up the word, but you only have a limitied number")
    print("of times to guess, so be careful!")
    print()

# Prints the number of lives the player has left
def evaluate_lives(lives):
    if lives == 1:
        print("You have 1 life remaining.")
    else:
        print(f"You have {lives} lives remaining.")

# Depending on the number of lives, prints a message accordingly
def won_game(word, lives):
    if lives == 0:
        print(f"Sorry, you lose! The word was: {word}")
        return False
    else:
        print("You win!")
        print(f"You ended the game with {lives} lives. Congratulations!")
        return True

# Asks the player if they want to play the game again
def play_again():
    answer = input("Would you like to play again? Type (y/n): ").lower()
    while answer not in ("y", "n"):
        print("Ivalid input. Try again!")
        answer = input("Would you like th play again? Type (y/n): ").lower()
    return answer == "y"

def choose_word(filename):
    dictionary = []
    with open(filename) as file:
        for line in file:
            dictionary.append(line)
    return random.choice(dictionary)

# Play a game of Hangman!
def play_game():

    # Creates a list of used letters
    used_letters = []

    # The word the user has to guess
    word = choose_word("4-lists/hangman/dict.txt")

    # This is the player's board, or the word replaced with blanks.
    # It will fill up with the letters that the player guesses correctly.
    player_board = ["_"] * (len(word) - 1)

    # Number of lives in the game
    lives = 6

    # Set the player score as a global variable for use around the code
    global player_score

    # The game plays until the whole word is guessed
    # or the player runs out of lives
    while "_" in player_board and lives != 0:
        print(f"{' '.join(player_board)}")
        player_input = input("Type any letter from A to Z: ").lower()

        # If the input is not something in the alphabet list, 
        # the player is prompted again for a valid input.
        while player_input in used_letters or len(player_input) > 1 or len(player_input) == 0:
            print("Letter has already been used or value is invalid! Try again.")
            print(f"{' '.join(player_board)}")
            player_input = input("Type another letter from A to Z: ")

        used_letters.append(player_input)

        # If the letter is not in the word, the player loses one life - 
        # otherwise, the blanks inside player_board will be filled with
        # the letter the user has inputted
        if player_input not in word:
            lives -= 1
            print("Your letter is not in the word! One life lost...")
        else:
            print("Your letter is in the word!")
            for i in range(len(word)):
                if word[i] == player_input:
                    player_board[i] = player_input

        # Evaluate the number of lives after every guess
        if lives != 0:
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
    print(f"Your score is: {player_score}")

main()