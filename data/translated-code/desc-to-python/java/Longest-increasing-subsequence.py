```python
def lis(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_lis = max(lis)
    result = []

    for i in range(n - 1, -1, -1):
        if lis[i] == max_lis:
            result.append(arr[i])
            max_lis -= 1

    result.reverse()
    return result

def main():
    arr1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    arr2 = [3, 10, 2, 1, 20]

    print("LIS for arr1: ", lis(arr1))
    print("LIS for arr2: ", lis(arr2))

if __name__ == "__main__":
    main()
```