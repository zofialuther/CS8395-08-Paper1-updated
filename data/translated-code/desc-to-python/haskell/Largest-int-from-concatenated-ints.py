```python
def sort_and_concatenate(lists):
    sorted_lists = [sorted(sublist) for sublist in lists]
    concatenated = ''.join([''.join(map(str, sublist)) for sublist in sorted_lists])
    return int(concatenated)

def main():
    example1 = [[3, 2, 1], [6, 5, 4]]
    example2 = [[9, 8, 7], [12, 11, 10]]
    result1 = sort_and_concatenate(example1)
    result2 = sort_and_concatenate(example2)
    print(result1)
    print(result2)

main()
```