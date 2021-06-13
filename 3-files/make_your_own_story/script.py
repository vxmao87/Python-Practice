# This method takes in words from the user and creates
# a story based on their input. The file uses word
# placeholders to create the story.

def print_intro():
    print("Create your own story by typing in your own words!")
    print("You won't know what the story says, so you'll be in for a surprise!")

def replace_word(line, file, target, input_word):
    for word in file.read().split():
        if word == target:
            return line.replace(target, input_word)


def write_story():
    adjective_1 = input("Type in an adjective: ")
    adjective_2 = input("Type in another adjective: ")
    # job = input("Type in a job or occupation: ")
    # place = input("Type in a place (a general area, not a country or city): ")
    # noun = input("Type a noun: ")
    # noun_plural = input("Type another noun in plural form: ")
    # adverb = input("Type an adverb: ")
    with open ("3-files/make_your_own_story/new_story.txt", "w") as outfile:
        with open ("3-files/make_your_own_story/story.txt") as file:
            for line in file:
                # outfile.write(line.replace("<adjective 1>", adjective_1))
                # outfile.write(line.replace("<adjective 2>", adjective_2))
                # outfile.write(line.replace("<job/occupation>", job))
                # outfile.write(line.replace("<place>", place))
                # outfile.write(line.replace("<noun>", noun))
                # outfile.write(line.replace("<plural-noun>", noun_plural))
                # outfile.write(line.replace("<adverb>", adverb))
                outfile.write(replace_word(line, file, "<adjective 1>", adjective_1))
                outfile.write(replace_word(line, file, "<adjective 2>", adjective_2))
        

def main():
    print_intro()
    write_story()

main()