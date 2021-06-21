# Play a game of tic-tac-toe with a friend using this program.

def print_intro():
    pass

# Determines if there is a win on the grid - in other words, if there is three of the same
# icon in any row, column, or diagonal
def wins(grid, player):
    icon = ""
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

# Takes in and returns the user's input for where they want their icon to be placed
def grab_position(pos):
    user_input = int(input("Type in the {} you want your icon on: ".format(pos)))
    while user_input < 0 or user_input > 2:
        print("Invalid input. Try again.")
        user_input = int(input("Type in the {} you want your icon on: ".format(pos)))
    return user_input

def is_empty(grid, row, column):
    return grid[row][column] == "_"

def play_game():
    grid = [["_"] * 3, ["_"] * 3, ["_"] * 3]
    print(grid)

    print(wins(grid, "1"))
    print(wins(grid, "2"))
    while not wins(grid, "1") and not wins(grid, "2"):
        if not wins(grid, "1"):
            row = grab_position("row")
            column = grab_position("column")
            input_list = []
            input_list.append(row)
            input_list.append(column)
            print(input_list)
            if is_empty(grid, row, column):
                grid[row][column] = "x"

            


def main():
    print_intro()
    play_game()

main()