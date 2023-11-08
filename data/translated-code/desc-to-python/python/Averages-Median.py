```python
def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

example_arr1 = [5, 2, 9, 1, 7]
example_arr2 = [3, 8, 4, 6, 10, 2]

median1 = median(example_arr1)
median2 = median(example_arr2)

print("Original array 1:", example_arr1)
print("Median of array 1:", median1)
print("Original array 2:", example_arr2)
print("Median of array 2:", median2)
```