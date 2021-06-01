def fraction_sum(n):
    if n < 1:
        raise ValueError("n must be greater than 0")
    total = 0
    for i in range(1, n + 1):
        # print(1/i)
        total += 1/i
    return total

def roman_numeral_converter(num):
    if num < 0 or num > 5000:
        raise ValueError("Your value must be greater than 0!")  
    currentNum = num
    result = ""
    if currentNum >= 1000:
        while currentNum >= 1000:
            currentNum -= 1000
            result += "M"
    if currentNum < 1000 and currentNum >= 500:
        while currentNum < 1000 and currentNum > 499:
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
    return result


def main():
    print(fraction_sum(10))
    print(roman_numeral_converter(901))

main()