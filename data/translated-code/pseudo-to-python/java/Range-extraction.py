arr = [1, 2, 3, 5, 6, 7, 9, 10, 11]
len = len(arr)
idx = 0
idx2 = 0
while idx < len:
    while idx2 < len and arr[idx2] - arr[idx2 - 1] == 1:
        idx2 += 1
    if idx2 - idx > 2:
        print(str(arr[idx]) + "-" + str(arr[idx2 - 1]) + ",")
        idx = idx2
    else:
        for val in range(idx, idx2):
            print(str(arr[idx]) + ",")
            idx += 1