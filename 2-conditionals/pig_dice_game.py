import random
import time

def print_intro():
    print("Welcome to Pig! Two players will each take turns rolling a die to earn")
    print("points. Be careful, though! If you roll a 1, you lose all the points")
    print("you obtained during that round! The first player to 100 points wins!")

def roll_dice(player):
    points = 0
    print("Player {} start!".format(player))
    repeat = "y"
    while repeat == "y":
        roll = random.randint(1, 6)
        time.sleep(1)
        if roll == 1:
            print("You rolled a 1!")
            points = 0
            repeat = "n"
        else:
            print("You rolled a {}.".format(roll))
            points += roll
            print("Your score for this round is currently {} point(s).".format(points))
            repeat = input("Would you like to roll again? (y/n)")
    print("Player {}, your turn is over!".format(player))
    time.sleep(1)
    return points

def play_game(limit):
    print("Type 'y' to begin: ")
    p1_points = 0
    p2_points = 0
    while p1_points < limit and p2_points < limit:
        if p1_points != 0:
            print("Player 1 has {} points.".format(p1_points))
            time.sleep(1)
        p1_points += roll_dice(1)
        print("Player 1 now has {} points.".format(p1_points))
        time.sleep(1)
        if p1_points < 100:
            if p2_points != 0:
                print("Player 2 has {} points.".format(p2_points))
                time.sleep(1)
            p2_points += roll_dice(2)
            print("Player 2 now has {} points.".format(p2_points))
            time.sleep(1)
    if p1_points > p2_points:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

def main():
    print_intro()
    limit = 100
    ready = input("Type y when you are ready to begin: ")
    while ready.lower() != "y":
        print("Invalid input. Try again.")
        ready = input("Type y when you are ready to begin: ")
    play_game(limit)

main()