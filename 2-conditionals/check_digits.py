# This method 

def main():
    print("This is a method.")
    studentCode = int(input("Please enter a six-digit code to determine the check digit."))
    # print(type(studentCode))
    if not isinstance(studentCode, int):
        raise TypeError("This value must be an integer!")
    if not number_of_digits(studentCode) == 6:
        raise ValueError("Your code must be 6 digits long!")
    sum = 0
    codeStr = str(studentCode)
    # print(codeStr)
    # print(isinstance(codeStr, str))
    for i in range(len(codeStr)):
        sum += (i + 1) * int(codeStr[i])
        # print((i + 1) * int(codeStr[i]))
    result = str(sum % 10)
    codeStr += result
    print("Your check digit is: ", result)
    print("The full code is:", codeStr)

# Checks the number of digits in the integer by performing
# floor division repeatedly on the integer
def number_of_digits(num):
    digits = 0
    while num > 0:
        digits = digits + 1
        num = num // 10
    return digits

main()