# This method reads a file and prints the number
# of words, lines and characters in the given file.

import os.path

def prompt_for_file(message):
    user_input = input(message)
    filename = "3-files/word_counter/{}".format(user_input)
    while not os.path.isfile(filename):
        print("File not found. Try again.")
        filename = input(message)
    return filename

def main():
    filename = prompt_for_file("File to open? ")
    word_count = 0
    line_count = 0
    char_count = 0
    with open(filename) as file:
        for line in file:
            line_count += 1
        print("Line count: ", line_count)


main()