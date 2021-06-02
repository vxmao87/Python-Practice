# This method accepts a number and reports the check digit for that number.
# Check digits are important for verification and integrity purposes.

def main():
    studentCode = int(input("Please enter a code to determine the check digit."))

    # The input MUST be an integer or an error will be raised
    if not isinstance(studentCode, int):
        raise TypeError("This value must be an integer!")
    
    # The sum of all values using the formula in the for loop below
    sum = 0

    # The inputted number is converted into a String under the variable name codeStr
    codeStr = str(studentCode)

    # The formula for calculating the check digit is as follows for
    # a number with n digits:
    # (n + 1)th digit = (1 x (1st digit) + 2 x (2nd digit) + ... + n x (nth digit)) % 10
    for i in range(len(codeStr)):
        sum += (i + 1) * int(codeStr[i])
    result = str(sum % 10)

    # Print the resulting check digit
    print("Your check digit is: ", result)

# Checks the number of digits in the integer by performing
# floor division by 10 repeatedly on the integer
def number_of_digits(num):
    digits = 0
    while num > 0:
        digits = digits + 1
        num = num // 10
    return digits

main()