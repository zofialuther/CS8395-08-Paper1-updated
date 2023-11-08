```python
def sort_disjoint(array, idxs):
    idxs.sort()
    disjoint = [array[idx] for idx in idxs]
    disjoint.sort()
    i = 0
    for idx in idxs:
        array[idx] = disjoint[i]
        i += 1

list = [7, 6, 5, 4, 3, 2, 1, 0]
indices = [6, 1, 7]
print(list)
sort_disjoint(list, indices)
print(list)
```