print("Let's do this!")

def print_nums():
    print("1, 2, 3, 4, 5")

def print_advice():
    print("There's one thing every coder must understand:")
    print("showing output with the print command")

def print_squares():
    for i in range(1, 25):
        print(i * i, end=" ")

# def print_figure1():
#     for i in range(7):
#         for j in range(7):

def print_numPyramid():
    for i in range(0, 8):
        print(i * i)

def main():
    print_nums()
    print_advice()
    print()
    print_advice()
    # print_figure1()
    print_squares()
    print_numPyramid()

main()