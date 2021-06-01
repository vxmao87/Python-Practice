def fraction_sum(n):
    if n < 1:
        raise ValueError("n must be greater than 0")
    total = 0
    for i in range(1, n + 1):
        # print(1/i)
        total += 1/i
    return total

def main():
    print(fraction_sum(10))

main()