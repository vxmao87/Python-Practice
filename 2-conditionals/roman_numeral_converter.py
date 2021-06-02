# This method takes in a number (from 1 to 4999) and converts it into Roman numerals.

def roman_numeral_converter():
    num = int(input("Type a number from 1 to 4999 to convert to Roman numerals: ")) 
    # Raises an error if input is not a number between 1 and 4999 
    if num <= 0 or num >= 5000:
        raise ValueError("Your value must be between 1 and 4999!")

    # currentNum is the inputted number which will be manipulated
    currentNum = num

    # The inputted number in Roman numerals
    result = ""

    # All 'if' statements below are used depending on the number given.
    # If currentNum falls within the given range, then the statements determine
    # how big the number is, subtract that value from currentNum and then add
    # the corresponding letters into the result string above.

    # If currentNum is between 1000 to 4999
    if currentNum >= 1000:
        while currentNum >= 1000:
            currentNum -= 1000
            result += "M"

    # If currentNum is between 500 to 999
    if currentNum < 1000 and currentNum >= 500:
        if currentNum >= 900:
            currentNum -= 900
            result += "CM"
        elif currentNum >= 800:
            currentNum -= 800
            result += "DCCC"
        elif currentNum >= 700:
            currentNum -= 700
            result += "DCC"
        elif currentNum >= 600:
            currentNum -= 600
            result += "DC"
        else:
            currentNum -= 500
            result += "D"
    
    # If currentNum is between 100 to 499
    if currentNum < 500 and currentNum >= 100:
        if currentNum >= 400:
            currentNum -= 400
            result += "CD"
        elif currentNum >= 300:
            currentNum -= 300
            result += "CCC"
        elif currentNum >= 200:
            currentNum -= 200
            result += "CC"
        else:
            currentNum -= 100
            result += "C"

    # If currentNum is between 50 to 99
    if currentNum < 100 and currentNum >= 50:
        if currentNum >= 90:
            currentNum -= 90
            result += "XC"
        elif currentNum >= 80:
            currentNum -= 80
            result += "LXXX"
        elif currentNum >= 70:
            currentNum -= 70
            result += "LXX"
        elif currentNum >= 60:
            currentNum -= 60
            result += "LX"
        else:
            currentNum -= 50
            result += "L"
    
    # If currentNum is between 10 to 49
    if currentNum < 50 and currentNum >= 10:
        if currentNum >= 40:
            currentNum -= 40
            result += "XL"
        elif currentNum >= 30:
            currentNum -= 30
            result += "XXX"
        elif currentNum >= 20:
            currentNum -= 20
            result += "XX"
        else:
            currentNum -= 10
            result += "X"

    # If currentNum is between 5 to 9
    if currentNum < 10 and currentNum >= 5:
        if currentNum == 9:
            currentNum -= 9
            result += "IX"
        elif currentNum == 8:
            currentNum -= 8
            result += "VIII"
        elif currentNum == 7:
            currentNum -= 7
            result += "VII"
        elif currentNum == 6:
            currentNum -= 6
            result += "VI"
        else:
            currentNum -= 5
            result += "V"

    # If currentNum is between 1 to 4
    if currentNum < 5 and currentNum > 0:
        if currentNum == 4:
            currentNum -= 4
            result += "IV"
        elif currentNum == 3:
            currentNum -= 3
            result += "III"
        elif currentNum == 2:
            currentNum -= 2
            result += "II"
        else:
            currentNum -= 1
            result += "I"
            
    print(result)


def main():
    roman_numeral_converter()

main()