# Play a game of tic-tac-toe with a friend using this program.

def print_intro():
    pass

def wins(grid, player):
    icon = "x"
    if player == "1":
        icon = "x"
    else:
        icon = "o"
    if (grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] == icon) or (grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] == icon) or (grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] == icon):
        return True
    elif (grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] == icon) or (grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] == icon) or (grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] == icon):
        return True
    elif (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] == icon) or (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] == icon):
        return True
    else:
        return False

def play_game():
    grid = [["_"] * 3, ["_"] * 3, ["_"] * 3]
    print(grid)

    print(wins(grid, "1"))
    print(wins(grid, "2"))
    while not wins(grid, "1") and not wins(grid, "2"):
        if not wins(grid, "1"):
            print("Type in two numbers, where the first number is the row you want to place your icon,")
            player_input = input("and the second number is the column you want to place your icon (1-3): ")
            


def main():
    print_intro()
    play_game()

main()