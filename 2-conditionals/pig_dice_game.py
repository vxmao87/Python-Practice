# This method plays a game of Pig, where two players take turns rolling a die
# until they reach 100 points. Any player who rolls a 1 during their turn will
# lose all the points for that round. Otherwise, they can roll as many times
# as they like. The point limit can be set for convenience.

import random
import time

# Prints the introduction to the game and program
def print_intro(limit):
    print("Welcome to Pig! Two players will each take turns rolling a die to earn")
    print("points. Be careful, though! If you roll a 1, you lose all the points")
    print("you obtained during that round! The first player to {} points wins!".format(limit))

# Either player takes their turn
def roll_dice(player):
    points = 0
    print("Player {} start!".format(player))

    # A state that determines whether it is still the current player's turn
    repeat = "y"

    while repeat == "y":

        # Roll a random number between 1 and 6 inclusive
        roll = random.randint(1, 6)
        time.sleep(1)

        # Player ends up with 0 points for a turn if a 1 is rolled
        if roll == 1:
            print("You rolled a 1!")
            points = 0
            repeat = "n"

        # Player gets points added to total score
        else:
            print("You rolled a {}.".format(roll))
            points += roll
            print("Your score for this round is currently {} point(s).".format(points))

            # If player types "y" they take another turn - if "n" their turn ends
            repeat = input("Would you like to roll again? (y/n)")

    # Ends the player's turn, returns the number of points gained
    print("Player {}, your turn is over!".format(player))
    time.sleep(1)
    return points

def play_game(limit):

    # Points for both players
    p1_points = 0
    p2_points = 0

    # Play the game while both players are under the point limit
    while p1_points < limit and p2_points < limit:

        # Player 1's turn
        if p1_points != 0:
            print("Player 1 has {} points.".format(p1_points))
        time.sleep(1)
        p1_points += roll_dice(1)
        print("Player 1 now has {} points.".format(p1_points))
        time.sleep(1)

        # If Player 1 has less than the point limit, Player 2 takes their turn
        if p1_points < limit:
            if p2_points != 0:
                print("Player 2 has {} points.".format(p2_points))
            time.sleep(1)
            p2_points += roll_dice(2)
            print("Player 2 now has {} points.".format(p2_points))
            time.sleep(1)

    # Determines the winner depending on each player's points
    if p1_points > p2_points:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

def main():

    # The number of points needed to win the game
    limit = 100

    print_intro(limit)

    # The user must type "y" or the game will not start
    ready = input("Type y when you are ready to begin: ")
    while ready.lower() != "y":
        print("Invalid input. Try again.")
        ready = input("Type y when you are ready to begin: ")

    # Play a game of Pig with the given point limit
    play_game(limit)

main()