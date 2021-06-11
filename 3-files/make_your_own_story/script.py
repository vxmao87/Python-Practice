# This method takes in words from the user and creates
# a story based on their input. The file uses word
# placeholders to create the story.

# Boilerplate code for verifying readable files
def prompt_for_file(message):
    user_input = input(message)
    filename = "3-files/make_your_own_story/{}".format(user_input)
    while not os.path.isfile(filename):
        print("File not found. Try again.")
        user_input = input(message)
        filename = "3-files/make_your_own_story/{}".format(user_input)
    return filename

def main():
    print("method")

main()