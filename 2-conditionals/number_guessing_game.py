import random

def play_game():
    number = random.randint(1, 100)
    guess = int(input("Guess my number! It will be between 1 and 100."))
    num_guesses = 1
    while guess != number:
        print("Incorrect.")
        guess = int(input("Guess my number again!"))
        num_guesses += 1
    print("Nice! You guessed my number in", num_guesses, "tries.")


def main():
    play_game()

main()