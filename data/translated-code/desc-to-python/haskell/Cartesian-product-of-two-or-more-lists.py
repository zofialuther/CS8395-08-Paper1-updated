```python
from itertools import product

def cartProdN(lists):
    return list(product(*lists))

def main():
    input_lists = [[1, 2, 3], [4, 5], [6, 7]]
    result = cartProdN(input_lists)
    print(result)

    empty_list = [[], [1, 2, 3]]
    result_empty = cartProdN(empty_list)
    print(result_empty)

if __name__ == "__main__":
    main()
```