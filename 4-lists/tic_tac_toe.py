# Play a game of tic-tac-toe with a friend using this program.

def print_intro():
    pass

def wins(grid):
    if (grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2]) or (grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2]) or (grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2]):
        return True
    elif (grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0]) or (grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1]) or (grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]):
        return True
    elif (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]) or (grid[0][2] == grid[1][1] and grid[1][1] == grid[3][0]):
        return True
    else:
        return False

def play_game():
    grid = [["_"] * 3, ["_"] * 3, ["_"] * 3]
    print(grid)

def main():
    print_intro()
    play_game()

main()