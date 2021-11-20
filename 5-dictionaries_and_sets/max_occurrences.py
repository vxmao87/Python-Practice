def max_occurrences(lis):
    if len(lis) == 0:
        return 0

    counts = {}
    highest_count = 0
    for num in lis:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        highest_count = max(highest_count, counts[num])

    return highest_count


    
lis_1 = [1, 3, 5, 8, 4, 8, 9, 4, 7, 2, 8, 5, 9, 1, 1, 1, 1]
lis_2 = []
lis_3 = [5, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]

print(max_occurrences(lis_1))
print(max_occurrences(lis_2))
print(max_occurrences(lis_3))