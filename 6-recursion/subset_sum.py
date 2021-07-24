# Finds the first subset in a list that adds up to the given target value
def subset_sum(list, target, length):

    # Traverse between two indexes
    for i in range(length):
        current_sum = list[i]
        j = i + 1

def main():
    list = [4, 6, 3, 2, 9, 3, 1, 6]
    length = len(list)
    target = 13
    subset_sum(list, target, length)

main()