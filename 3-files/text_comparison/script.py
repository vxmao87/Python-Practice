# This program compares two readable files and
# prints any differences between them.

import os.path

def print_intro():
    print("Check any two documents to see if there are any")
    print("differences between the two!")

# Boilerplate code for verifying readable files
def prompt_for_file(message):
    user_input = input(message)
    filename = "3-files/text-comparison/{}".format(user_input)
    while not os.path.isfile(filename):
        print("File not found. Try again.")
        filename = input(message)
    return filename

def main():
    print_intro()
    filename_1 = prompt_for_file("Enter a first file name: ")
    filename_2 = prompt_for_file("Enter a second file name: ")
    

main()