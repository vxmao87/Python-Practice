def list_range(lis):
    # min = lis[0]
    # max = lis[0]
    # for i in range(len(lis)):
    #     if lis[i] > max:
    #         max = lis[i]
    #     if lis[i] < min:
    #         min = lis[i]
    # return max - min + 1
    return max(lis) - min(lis) + 1

def is_sorted(lis):
    if len(lis) == 1:
        return True
    current_num = lis[0]
    for i in range(len(lis)):
        if lis[i] < current_num:
            return False
        else:
            current_num = lis[i]
    return True

def mode(lis):
    tally = [0] * max(lis)
    for i in range(len(lis)):
        tally[lis[i] - 1] += 1
    return tally.index(max(tally)) + 1

def median(lis):
    new_lis = sorted(lis)
    return new_lis[len(new_lis) // 2]

def price_is_right(bids, correct_bid):
    best_bid = -1
    for i in range(len(bids)):
        if bids[i] <= correct_bid and bids[i] > best_bid:
            best_bid = bids[i]
    return best_bid

def collapse(lis):
    final_lis = [0] * ((len(lis) + 1) // 2)
    lis_len = 0
    for i in range(0, len(lis) - 1, 2):
        final_lis[lis_len] = lis[i] + lis[i + 1]
        lis_len += 1
    if lis_len != len(final_lis):
        final_lis[lis_len] = lis[-1]
    return final_lis

def vowel_count(str):
    final_lis = [0] * 6
    for c in str:
        if c.lower() == "a":
            final_lis[0] += 1
        elif c.lower() == "e":
            final_lis[1] += 1
        elif c.lower() == "i":
            final_lis[2] += 1
        elif c.lower() == "o":
            final_lis[3] += 1
        elif c.lower() == "u":
            final_lis[4] += 1
        elif c.lower() == "y":
            final_lis[5] += 1
    return final_lis

def min_to_front(lis):
    min = lis[0]
    index = 0
    for i in range(1, len(lis)):
        if lis[i] < min:
            min = lis[i]
            index = i
    lis.pop(index)
    lis.insert(0, min)
    return lis

def remove_even_length(lis):
    for i in range(len(lis)):
        if len(lis[1]) % 2 == 0:
            lis.pop(i)
    return lis

def double_list(lis):
    for i in range(0, len(lis) + 2, 2):
        lis.insert(i + 1, lis[i])
    return lis

def scale_by_k(lis):
    length = len(lis)
    index = 0
    for i in range(0, length):
        if lis[i] > 0:
            for j in range(lis[i] - 1):
                lis.insert(index, lis[i])
                i += 1
    return lis

def main():

    print(list_range([36, 12, 25, 19, 46, 31, 22]))

    print(is_sorted([16.1, 12.3, 22.2, 14.4]))
    print(is_sorted([1.5, 4.3, 7.0, 19.5, 25.1, 46.2]))
    print(is_sorted([23]))
    print(is_sorted([23, 25]))

    print("The mode of the list is", mode([27, 15, 15, 11, 27]))

    print("The first median is", median([5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17]))
    print("The second median is", median([42, 37, 1, 97, 1, 2, 7, 42, 3, 25, 89, 15, 10, 29, 27]))

    bids = [200, 300, 250, 1, 950, 40]
    print(price_is_right(bids, 280), "is the closest bid.")

    print(collapse([7, 2, 8, 9, 4, 13, 7, 1, 9, 10]))
    print(collapse([1, 2, 3, 4, 5]))

    print("Vowel counts:", vowel_count("i think, therefore i am"))
    print("Vowel counts:", vowel_count("you miss 100 percent of the shots you don't take"))

    print(min_to_front([3, 8, 92, 4, 2, 17, 9]))
    print(min_to_front([23, 67, 45, 90, 31, 18, 56, 45]))

    print(remove_even_length(["scintillate", "obsequious", "omnipotent", "vitiate", "piquant", "melee", "sidereal"]))

    print(double_list(["how", "are", "you?"]))

    print(scale_by_k([4, 1, 2, 0, 3]))

main()