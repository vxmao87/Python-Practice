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

def print_numBox(n):
    for i in range(1, n + 1):
        print("[", i, "]")

def print_only(number):
    if number > 0:
        print("Number is positive.")
    elif number == 0:
        print("Number is neither positive nor negative.")
    else:
        print("Number is negative.")

def print_powers_of_n(num1, num2):
    for i in range(0, num2 + 1):
        print(pow(num1, i), end=" ")

def main():
    print_nums()
    print_advice()
    print()
    print_advice()
    # print_figure1()
    print_squares()
    print_numPyramid()
    print_numBox(15)
    print_only(10)
    print_only(0)
    print_only(-10)
    print_powers_of_n(5, 6)

main()