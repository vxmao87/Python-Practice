# This program compares two readable files and
# prints any differences between them.

import os.path

# Prints the introduction for the program
def print_intro():
    print("Check any two documents to see if there are any")
    print("differences between the two!")

# Boilerplate code for verifying readable files
def prompt_for_file(message):
    user_input = input(message)
    filename = "3-files/text_comparison/{}".format(user_input)
    while not os.path.isfile(filename):
        print("File not found. Try again.")
        user_input = input(message)
        filename = "3-files/text_comparison/{}".format(user_input)
    return filename

def main():
    print_intro()

    # Asks for the names of both files
    filename_1 = prompt_for_file("Enter a first file name: ")
    filename_2 = prompt_for_file("Enter a second file name: ")

    # Counter for difference labeling purposes
    differences = 0

    # Opens both files and through a nested loop,
    # compares the lines of both files - if the lines
    # are different, print both of them - regardless
    # of outcome, break the conditional and move onto
    # the next line in both documents
    with open(filename_1) as file_1:
        with open(filename_2) as file_2:
            for line_1 in file_1:
                for line_2 in file_2:
                    if line_1 != line_2:
                        differences += 1
                        if differences == 1:
                            print("Differences found: ")
                        print("Difference #{}:".format(differences))
                        print("> {}".format(line_1), end = "\n")
                        print("< {}".format(line_2), end = "\n")
                    break

    # Prints a different message if there are no differences
    # found between both files
    if differences == 0:
        print("No differences found.")

main()