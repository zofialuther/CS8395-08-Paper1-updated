```python
def bSearch(compare, arr, lower, upper):
    while lower <= upper:
        mid = (lower + upper) // 2
        if compare(arr[mid]) == 0:
            return mid
        elif compare(arr[mid]) < 0:
            upper = mid - 1
        else:
            lower = mid + 1
    return None

def bSearchArray(arr, elem):
    def compare(value):
        if value == elem:
            return 0
        elif value < elem:
            return -1
        else:
            return 1
    return bSearch(compare, arr, 0, len(arr) - 1)

# Test scenario
strings = ["apple", "banana", "cherry", "date", "fig", "grape"]
search_elem = "date"
index = bSearchArray(strings, search_elem)
if index is not None:
    print(f"The element {search_elem} was found at index {index}.")
else:
    print(f"The element {search_elem} was not found.")
```