```python
def lexicographical_sort(lst):
    return sorted(map(str, lst), key=str) 

def create_list():
    return [5, 2, 9, 4, 7]

def test():
    numbers = create_list()
    sorted_numbers = lexicographical_sort(numbers)
    print(sorted_numbers)

def main():
    test()

if __name__ == "__main__":
    main()
```