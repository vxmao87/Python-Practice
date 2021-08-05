# Finds the first subset in a list that adds up to the given target value
def subset_sum(list, target, length):

    # Final subset
    big_set = []

    # Traverse between two indexes by first looking
    # at all subsets starting at 'i'
    for i in range(length):

        # Add the value to the final subset first
        big_set.append(list[i])

        current_sum = list[i]
        j = i + 1

        while j <= length:
            print(list[i])

            # The first subset to match the tagret sum is returned
            if current_sum == target:
                return big_set
            
            # Break out of the loop if either the sum is too big
            # or loop reaches the end of the list
            if current_sum > target or j == length:
                big_set.clear()
                break

            # Add the next value to the current sum, append the added value
            # onto the final subset, and look at the next value in the list
            current_sum = current_sum + list[j]
            big_set.append(list[j])
            j += 1
    
    # Return an empty list
    return "[]"


def main():
    list = [4, 2, 3, 2, 9, 3, 1, 6]
    length = len(list)
    target = 15
    print(target, "=", subset_sum(list, target, length))

main()