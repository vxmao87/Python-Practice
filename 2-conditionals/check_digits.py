def main():
    print("This is a method.")
    studentCode = int(input("Please enter a six-digit student code to determine the check digit."))
    print(type(studentCode))
    if not instanceof(studentCode, int):
        raise TypeError("This value must be an integer!")
    if not number_of_digits(studentCode) == 6:
        raise ValueError("Your student code must be 6 digits long!")
    sum = 0   

def number_of_digits(num):
    digits = 0
    while num > 0:
        digits = digits + 1
        num = num // 10
    return digits

main()