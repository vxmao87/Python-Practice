import random

def print_intro():
    print("Welcome to Pig! Two players will each take turns rolling a die to earn")
    print("points. Be careful, though! If you roll a 1, you lose all the points")
    print("you obtained during that round! The first player to 100 points wins!")

def roll_dice(player):
    points = 0
    print("Player {} start!".format(player))
    repeat = "y"
    while repeat == "y":
        roll = random.randint(1, 7)
        if roll == 1:
            print("You rolled a 1!")
            points = 0
            repeat = "n"
        else:
            print("You rolled a {}.".format(roll))
            points += roll
            print("Your score for this round is currently {} point(s).")
            repeat = input("Would you like to roll again? (y/n)")
    print("Player {}, your turn is over!")
    return points


def play_game():
    print("Type 'y' to begin: ")
    p1_points = 0
    p2_points = 0
    while p1_points < 100 and p2_points < 100:
        print("Player 1 has {} points, and Player 2 has {} points.".format(p1_points, p2_points))
        p1_points += roll_dice()

def main():
    print_intro()
    ready = input("Type y when you are ready to begin: ")
    while ready.lower() != "y":
        print("Invalid input. Try again.")
        ready = input("Type y when you are ready to begin: ")
    play_game()

main()