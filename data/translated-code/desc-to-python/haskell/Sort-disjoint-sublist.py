```python
def disSort1(arr, indices):
    # partition the list based on the given indices
    # sort the sublist
    # merge it with the rest of the list
    pass

def disSort2(arr, indices):
    # convert the list to an array
    # extract the sublist based on the indices
    # sort it
    # replace the elements in the original array
    pass

def disSort3(arr, indices):
    # achieve similar results as disSort2
    # but use mutable arrays for in-place updating
    pass

def main():
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample_indices = [2, 5, 8]
    disSort1(sample_list, sample_indices)
    disSort2(sample_list, sample_indices)
    disSort3(sample_list, sample_indices)

if __name__ == "__main__":
    main()
```