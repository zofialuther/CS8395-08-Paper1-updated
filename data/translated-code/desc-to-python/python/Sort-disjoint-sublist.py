```python
def disjointSort(arr, indexes):
    sublist = [arr[i] for i in indexes]
    sorted_sublist = sorted(sublist)
    result = arr.copy()
    for i, index in enumerate(indexes):
        result[index] = sorted_sublist[i]
    return result

def main():
    arr1 = [7, 6, 5, 4, 3, 2, 1, 0]
    arr2 = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    indexes = [6, 1, 7]
    print("Original List 1:", arr1)
    print("Disjoint Sorted List 1:", disjointSort(arr1, indexes))
    print("Original List 2:", arr2)
    print("Disjoint Sorted List 2:", disjointSort(arr2, indexes))

main()
```