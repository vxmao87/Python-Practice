# This method accepts a number and reports the check digit for that number.
# Check digits are important for verification and integrity purposes.

def main():
    student_code = int(input("Please enter a code to determine the check digit."))

    # The input MUST be an integer or an error will be raised
    if not isinstance(student_code, int):
        raise TypeError("This value must be an integer!")
    
    # The sum of all values using the formula in the for loop below
    current_sum = 0

    # The inputted number is converted into a String under the variable name code_str
    code_str = str(student_code)

    # The formula for calculating the check digit is as follows for
    # a number with n digits:
    # (n + 1)th digit = (1 x (1st digit) + 2 x (2nd digit) + ... + n x (nth digit)) % 10
    for i in range(len(code_str)):
        current_sum += (i + 1) * int(code_str[i])
    result = str(current_sum % 10)

    # Print the resulting check digit
    print("Your check digit is: ", result)

main()