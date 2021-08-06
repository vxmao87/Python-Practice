# from DrawingPanel import *

def list_range(lis):
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

def contains(a1, a2):
    if len(a2) == 0:
        return True
    if len(a1) == 0 and len(a2) != 0:
        return False

    for i in range(len(a1) - len(a2) + 1):
        count = 0
        for j in range(len(a2)):
            if a1[i + j] == a2[j]:
                count += 1
        if count == len(a2):
            return True
    
    return False

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

# Incomplete
def scale_by_k(lis):
    length = len(lis)
    index = 0
    for i in range(0, length):
        if lis[i] > 0:
            for j in range(lis[i] - 1):
                lis.insert(index, lis[i])
                i += 1
    return lis

def remove_duplicates(lis):
    lis = sorted(lis)
    length = len(lis)
    for i in range(length - 2):
        if lis[i] == lis[i + 1]:
            lis.pop(i + 1)
    return lis

def matrix_add(m_1, m_2):
    if len(m_1) != len(m_2) or len(m_1[0]) != len(m_2[0]):
        raise TypeError("Both matrices must be the same dimension!")
    m_3 = []
    for a in range(len(m_1)):
        m_3.append([0] * len(m_1[0]))
    for i in range(0, len(m_1)):
        for j in range(0, len(m_1[0])):
            m_3[i][j] = m_1[i][j] + m_2[i][j]
    return m_3

def is_magic_square(lis):
    # Use the sum of the first row as the magic number
    target_sum = sum(lis[0])

    # Check that all rows add up to the magic number
    for i in range(len(lis)):
        if sum(lis[i]) != target_sum:
            return False

    # Check that all columns add up to the magic number
    for a in range(len(lis)):
        new_sum = 0
        for b in range(len(lis[0])):
            new_sum += lis[b][a]
        if new_sum != target_sum:
            return False

    # Check that the diagonal from the left adds to the magic number
    new_sum_2 = 0
    for c in range(len(lis)):
        new_sum_2 += lis[c][c]
    if new_sum_2 != target_sum:
        return False

    # Check that the diagonal from the right adds to the magic number
    new_sum_3 = 0
    for d in range(len(lis)):
        new_sum_3 += lis[d][len(lis) - 1 - d]
    if new_sum_3 != target_sum:
        return False

    return True

# def grayscale(panel):
#     px = panel.pixels
#     for x in range(panel.width):
#         for y in range(panel.height):
#             r, g, b = px[x][y]
#             scale = (r + g + b) / 3
#             px[x][y] = (scale, scale, scale)
#     panel.pixels = px

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

    a1 = [1, 6, 2, 1, 4, 1, 2, 1, 8]
    a2 = [1, 2, 1]
    b2 = [1, 5, 1]
    print("Does this contain this?", contains(a1, a2))
    print("Does this contain this?", contains(a1, b2))

    print(collapse([7, 2, 8, 9, 4, 13, 7, 1, 9, 10]))
    print(collapse([1, 2, 3, 4, 5]))

    print("Vowel counts:", vowel_count("i think, therefore i am"))
    print("Vowel counts:", vowel_count("you miss 100 percent of the shots you don't take"))

    print(min_to_front([3, 8, 92, 4, 2, 17, 9]))
    print(min_to_front([23, 67, 45, 90, 31, 18, 56, 45]))

    print(remove_even_length(["scintillate", "obsequious", "omnipotent", "vitiate", "piquant", "melee", "sidereal"]))

    print(double_list(["how", "are", "you?"]))

    print(scale_by_k([4, 1, 2, 0, 3]))

    print(remove_duplicates(["be", "be", "is", "not", "or", "question", "that", "the", "to", "to"]))

    m_1 = [[2, 5, 6], [7, 4, 9], [10, 1, 6]]
    m_2 = [[1, 7, 4], [2, 9, 5], [20, 25, 13]]
    print(matrix_add(m_1, m_2))

    print(is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))

main()