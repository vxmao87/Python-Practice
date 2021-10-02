def list_range(lis):
    return max(lis) - min(lis)

def is_sorted(lis):
    if len(lis) == 1:
        return True
    current_num = lis[0]
    for i in range(len(lis) - 1):
        if current_num > lis[i + 1]:
            return False
        current_num = lis[i]
    return True

def mode(lis):
    tally = [0] * 100
    for i in range(len(lis)):
        value = lis[i]
        tally[value - 1] += 1
    return tally.index(max(tally)) + 1

def median(lis):
    new_lis = sorted(lis)
    if not len(lis) % 2 == 0:
        num = int((len(lis) - 1) / 2)
        return new_lis[num]

def price_is_right(bids, price):
    prices = []
    price_dif = []
    for i in range(len(bids)):
        if bids[i] <= price:
            prices.append(bids[i])
            price_dif.append(price - bids[i])
    if len(price_dif) == 0:
        return -1
    else:
        return prices[price_dif.index(min(price_dif))]

def collapse(lis):
    new_lis = []
    for i in range(int(len(lis) / 2)):
        new_lis.append(lis[i * 2] + lis[i * 2 + 1])
    if not len(lis) % 2 == 0:
        new_lis.append(lis[-1])
    return new_lis

def vowel_count(text):
    tally = [0] * 5
    for c in text:
        if c == "a":
            tally[0] += 1
        elif c == "e":
            tally[1] += 1
        elif c == "i":
            tally[2] += 1
        elif c == "o":
            tally[3] += 1
        elif c == "u":
            tally[4] += 1
    return tally

def min_to_front(lis):
    num = lis.pop(lis.index(min(lis)))
    lis.insert(0, num)
    return lis

def remove_even_length(lis):
    index = 0
    while not index >= len(lis):
        if len(lis[index]) % 2 == 0:
            lis.pop(index)
        else:
            index += 1
    return lis

def double_list(lis):
    index = 0
    while not index >= len(lis):
        lis.insert(index, lis[index])
        index += 2
    return lis

def scale_by_k(lis):
    index = 0
    while not index >= len(lis):
        if lis[index] <= 0:
            lis.pop(index)
        else:
            for i in range(lis[index] - 1):
                lis.insert(index, lis[index])
            index += lis[index]
    return lis

def main():
    print("The range is", list_range([36, 12, 25, 19, 46, 31, 22, 11]))
    print(is_sorted([16.1, 12.3, 22.2, 14.4]))
    print(is_sorted([1.5, 4.3, 7.0, 19.5, 25.1, 46.2]))
    print(mode([27, 15, 15, 11, 27]))
    print(median([5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17]))
    print(median([42, 37, 1, 97, 1, 2, 7, 42, 3, 25, 89, 15, 10, 29, 27]))
    print(price_is_right([200, 300, 250, 1, 950, 40], 250))
    print(price_is_right([200, 300, 250, 100, 950, 40], 20))

    print(collapse([7, 2, 8, 9, 4, 13, 7, 1, 9, 10]))
    print(collapse([1, 2, 3, 4, 5]))

    print("Vowel count:", vowel_count("i think, therefore i am"))

    print(min_to_front([3, 8, 92, 4, 2, 17, 9]))

    print(remove_even_length(["pastel", "tired", "correlate", "skid", "pass"]))

    print(double_list(["how", "are", "you"]))

    print(scale_by_k([4, 0, 0, 0, 1, 2, -5, 0, -10, -45, -2, 3]))

main()