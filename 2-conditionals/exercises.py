import random

def fraction_sum(n):
    if n < 1:
        raise ValueError("n must be greater than 0")
    total = 0
    for i in range(1, n + 1):
        # print(1/i)
        total += 1/i
    return total

def longest_name(times):
    if times < 0:
        raise ValueError("Method will not run...")
    longest_name = ""
    for i in range(1, times + 1):
        name = input("name? ")
        if len(name) > len(longest_name):
            longest_name = name
    print(str.capitalize(longest_name),"'s name is longest")

def smallest_largest():
    times = int(input("How many numbers do you want to enter? "))
    largest = 0
    smallest = 0
    for i in range(1, times + 1):
        user_num = int(input("Number ", i))
        if user_num > largest:
            largest = user_num
        elif user_num < smallest:
            smallest = user_num
    print("Smallest = ", smallest)
    print("Largest = ", largest)

def dice_sum():
    user_sum = int(input("Desired dice sum: "))
    sum_1 = random.randint(1, 6)
    sum_2 = random.randint(1, 6)



def main():
    print(fraction_sum(10))
    longest_name(3)
    smallest_largest()
    dice_sum()

main()