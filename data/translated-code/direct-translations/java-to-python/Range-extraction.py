def main():
    arr = [0, 1, 2, 4, 6, 7, 8, 11, 12, 14,
           15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
           25, 27, 28, 29, 30, 31, 32, 33, 35, 36,
           37, 38, 39]

    len_arr = len(arr)
    idx = 0
    idx2 = 0
    while idx < len_arr:
        while idx2 < len_arr and arr[idx2] - arr[idx2 - 1] == 1:
            idx2 += 1
        if idx2 - idx > 2:
            print(f"{arr[idx]}-{arr[idx2 - 1]},", end="")
            idx = idx2
        else:
            for i in range(idx, idx2):
                print(f"{arr[i]},", end="")
            idx = idx2

main()