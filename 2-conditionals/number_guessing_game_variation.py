# This method plays a variation of the number-guessign game with the user.
# The user will pick a number between 1 and 100, and the program will
# try to guess the user's number. The user can tell the program whether
# its number is higher or lower that the user's actual number.

def print_intro():
    print("Think of any number between 1 and 100, and you can tell me")
    print("whether my guess is higher or lower than your number!")

def play_game():
    

def main():
    print_intro()
    ready = input("Type y when you are ready with your number: ")
    while ready.lower() != "y":
        print("Invalid input. Try again.")
        ready = input("Type y when you are ready with your number: ")
    play_game()
    
main()