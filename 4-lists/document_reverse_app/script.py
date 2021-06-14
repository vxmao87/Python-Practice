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
            reversed_doc.append(line.rstrip().split())
    print(reversed_doc)
    reversed_doc.reverse()
    print(reversed_doc)
    for i in range(len(reversed_doc)):
        reversed_doc[i].reverse()
    print(reversed_doc)

main()