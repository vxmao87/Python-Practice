# This method reads a file and prints the number
# of words, lines and characters in the given file.

import os.path

# Boilerplate code for verifying readable files
def prompt_for_file(message):
    user_input = input(message)
    filename = "3-files/word_counter/{}".format(user_input)
    while not os.path.isfile(filename):
        print("File not found. Try again.")
        user_input = input(message)
        filename = "3-files/word_counter/{}".format(user_input)
    return filename

def main():
    filename = prompt_for_file("File to open? ")

    # Counters for lines, words and characters
    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename) as file:
        for line in file:

            # Removes all "newline" instances so that the input is all one line
            line = line.strip("\n")

            # Returns a list of words in the given line by disregarding whitespace
            words = line.split()

            line_count += 1            
            word_count += len(words)
            char_count += len(line)

        # Prints the number of lines, words and characters in the document    
        print("Line count: ", line_count)
        print("Word count: ", word_count)
        print("Character count: ", char_count)


main()