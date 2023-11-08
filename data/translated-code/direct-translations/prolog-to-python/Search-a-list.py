```python
def search_a_list(N1, N2):
    L = ["Zig", "Zag", "Wally", "Ronald", "Bush", "Krusty", "Charlie", "Bush", "Boz", "Zag"]
    
    print('List is :', end='')
    for name in L:
        my_write(name)
    print('\n')

    try:
        Ind1 = L.index(N1) + 1
        print(f'{N1} is in position {Ind1}')
    except ValueError:
        print(f'{N1} is not present')

    try:
        Ind2 = L.index(N2) + 1
        print(f'{N2} is in position {Ind2}')
    except ValueError:
        print(f'{N2} is not present')

    try:
        Ind3 = len(L) - L[::-1].index(N1)
        print(f'{N1} last position is {Ind3}')
    except ValueError:
        print(f'{N1} is not present')

def my_write(Name):
    print(f' {Name}', end='')
```