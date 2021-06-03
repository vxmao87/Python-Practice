# This method takes in a number (from 1 to 4999) and converts it into Roman numerals.

def roman_numeral_converter():
    num = int(input("Type a number from 1 to 4999 to convert to Roman numerals: ")) 
    # Raises an error if input is not a number between 1 and 4999 
    if num <= 0 or num >= 5000:
        raise ValueError("Your value must be between 1 and 4999!")

    # current_num is the inputted number which will be manipulated
    current_num = num

    # The inputted number in Roman numerals
    result = ""

    # All 'if' statements below are used depending on the number given.
    # If current_num falls within the given range, then the statements determine
    # how big the number is, subtract that value from current_num and then add
    # the corresponding letters into the result string above.

    # If current_num is between 1000 to 4999
    if current_num >= 1000:
        while current_num >= 1000:
            current_num -= 1000
            result += "M"

    # If current_num is between 500 to 999
    if current_num < 1000 and current_num >= 500:
        if current_num >= 900:
            current_num -= 900
            result += "CM"
        elif current_num >= 800:
            current_num -= 800
            result += "DCCC"
        elif current_num >= 700:
            current_num -= 700
            result += "DCC"
        elif current_num >= 600:
            current_num -= 600
            result += "DC"
        else:
            current_num -= 500
            result += "D"
    
    # If current_num is between 100 to 499
    if current_num < 500 and current_num >= 100:
        if current_num >= 400:
            current_num -= 400
            result += "CD"
        elif current_num >= 300:
            current_num -= 300
            result += "CCC"
        elif current_num >= 200:
            current_num -= 200
            result += "CC"
        else:
            current_num -= 100
            result += "C"

    # If current_num is between 50 to 99
    if current_num < 100 and current_num >= 50:
        if current_num >= 90:
            current_num -= 90
            result += "XC"
        elif current_num >= 80:
            current_num -= 80
            result += "LXXX"
        elif current_num >= 70:
            current_num -= 70
            result += "LXX"
        elif current_num >= 60:
            current_num -= 60
            result += "LX"
        else:
            current_num -= 50
            result += "L"
    
    # If current_num is between 10 to 49
    if current_num < 50 and current_num >= 10:
        if current_num >= 40:
            current_num -= 40
            result += "XL"
        elif current_num >= 30:
            current_num -= 30
            result += "XXX"
        elif current_num >= 20:
            current_num -= 20
            result += "XX"
        else:
            current_num -= 10
            result += "X"

    # If current_num is between 5 to 9
    if current_num < 10 and current_num >= 5:
        if current_num == 9:
            current_num -= 9
            result += "IX"
        elif current_num == 8:
            current_num -= 8
            result += "VIII"
        elif current_num == 7:
            current_num -= 7
            result += "VII"
        elif current_num == 6:
            current_num -= 6
            result += "VI"
        else:
            current_num -= 5
            result += "V"

    # If current_num is between 1 to 4
    if current_num < 5 and current_num > 0:
        if current_num == 4:
            current_num -= 4
            result += "IV"
        elif current_num == 3:
            current_num -= 3
            result += "III"
        elif current_num == 2:
            current_num -= 2
            result += "II"
        else:
            current_num -= 1
            result += "I"
            
    print(result)


def main():
    roman_numeral_converter()

main()