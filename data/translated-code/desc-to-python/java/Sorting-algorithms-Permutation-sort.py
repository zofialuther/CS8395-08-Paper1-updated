```python
def pSort(arr):
    if arr == sorted(arr):
        return arr
    else:
        return pSort(arr[1:]) + [arr[0]]

arr = [3, 1, 5, 4, 2]
arr = pSort(arr)
print(arr)
```