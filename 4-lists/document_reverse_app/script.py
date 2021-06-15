# This program reverses the lines in a given document, along with
# every word in each line. Lists are utilized.

import os.path

# Boilerplate code for verifying readable files
def prompt_for_file(message):
    user_input = input(message)
    filename = "4-lists/document_reverse_app/{}".format(user_input)
    while not os.path.isfile(filename):
        print("File not found. Try again.")
        user_input = input(message)
        filename = "4-lists/document_reverse_app/{}".format(user_input)
    return filename

def main():
    filename = prompt_for_file("Enter a filename to reverse the contents of: ")

    # The final reversed document in list form
    reversed_doc = []

    # Adds every line in document into the list, separated by each word. The
    # appended sentences are also stored as an individual list.
    with open(filename) as file:
        for line in file:
            reversed_doc.append(line.split())

    # Adds a newline next to the last element in each list, which will
    # cause the result to start a new line when printing the final document
    for i in range(len(reversed_doc)):
        reversed_doc[i].reverse()
        reversed_doc[i][-1] += "\n"

    # Adds a space to the right of every element in every sentence except
    # for the very last element in each sentence (the previous method already
    # accounts for that)
    for i in range(len(reversed_doc)):
        for j in range(len(reversed_doc[i]) - 1):
                reversed_doc[i][j] += " "

    # Reverses the order of all sentences
    reversed_doc.reverse()

    # Writes the line-reversed, sentence-reversed result into a new file
    with open("4-lists/document_reverse_app/new_story.txt", "w") as outfile:
        for i in range(len(reversed_doc)):
            for j in range(len(reversed_doc[i])):
                outfile.write(reversed_doc[i][j])
                
main()