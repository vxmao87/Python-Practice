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
    reversed_doc = []
    with open(filename) as file:
        for line in file:
            reversed_doc.append(line.split())
    for i in range(len(reversed_doc)):
        reversed_doc[i].reverse()
        reversed_doc[i][-1] += "\n"
    for i in range(len(reversed_doc)):
        for j in range(len(reversed_doc[i]) - 1):
                reversed_doc[i][j] += " "
    with open("4-lists/document_reverse_app/new_story.txt", "w") as outfile:
        for i in range(len(reversed_doc)):
            for j in range(len(reversed_doc[i])):
                outfile.write(reversed_doc[i][j])
main()