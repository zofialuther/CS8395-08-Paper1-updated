```python
def rotate_list(lst, n):
    return lst[-n:] + lst[:-n]

def rotate_list_of_lists(list_of_lists, rotations):
    return [rotate_list(sublist, rotation) for sublist, rotation in zip(list_of_lists, rotations)]

def append_lists(lst1, lst2):
    return lst1 + lst2

def identity_matrix(size):
    return [rotate_list([1] + [0]*(size-1), i) for i in range(size)]

def main():
    result = identity_matrix(5)
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
```