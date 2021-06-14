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

def main():

    print(list_range([36, 12, 25, 19, 46, 31, 22]))

    print(is_sorted([16.1, 12.3, 22.2, 14.4]))
    print(is_sorted([1.5, 4.3, 7.0, 19.5, 25.1, 46.2]))
    print(is_sorted([23]))
    print(is_sorted([23, 25]))

    print(mode([27, 15, 15, 11, 27]))

    print(median([5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17]))
    print(median([42, 37, 1, 97, 1, 2, 7, 42, 3, 25, 89, 15, 10, 29, 27]))

    bids = [200, 300, 250, 1, 950, 40]
    print(price_is_right(bids, 280))

    print(collapse([7, 2, 8, 9, 4, 13, 7, 1, 9, 10]))
    print(collapse([1, 2, 3, 4, 5]))

main()