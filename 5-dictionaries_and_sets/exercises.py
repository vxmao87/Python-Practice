def exper(arrival, duration):
    new_list = []
    for i in range(len(arrival)):
        lis = []
        lis.append(arrival[i])
        lis.append(duration[i])
        new_list.append(lis)
    print(new_list)
    new_list.sort()
    print(new_list)
    print(new_list[2][0])

def main():
    arr = [1, 3, 3, 5, 7]
    dur = [2, 2, 1, 2, 1]
    exper(arr, dur)

main()