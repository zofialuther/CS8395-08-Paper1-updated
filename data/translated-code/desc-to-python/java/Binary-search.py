```python
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    x = 7
    result = binarySearch(arr, x)
    print("Index of", x, "is", result)

if __name__ == "__main__":
    main()
```