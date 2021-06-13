# This method takes in words from the user and creates
# a story based on their input. The file uses word
# placeholders to create the story.

def print_intro():
    print("Create your own story by typing in your own words!")
    print("You won't know what the story says, so you'll be in for a surprise!")

def write_story():
    adjective_1 = input("Type in an adjective: ")
    adjective_2 = input("Type in another adjective: ")
    job = input("Type in a job or occupation: ")
    place = input("Type in a place (a general area, not a country or city): ")
    noun = input("Type a noun: ")
    noun_plural = input("Type another noun in plural form: ")
    adverb = input("Type an adverb: ")
    replacements = {"<adjective 1>":adjective_1, "<adjective 2>":adjective_2, "<job/occupation>":job, "<place>":place, "<noun>":noun, "<plural-noun>":noun_plural, "<adverb>":adverb}
    with open ("3-files/make_your_own_story/new_story.txt", "w") as outfile:
        with open ("3-files/make_your_own_story/story.txt") as file:
            for line in file:
                for target_word, input_word in replacements.items():
                    line = line.replace(target_word, input_word)
                outfile.write(line)

def main():
    print_intro()
    write_story()

main()