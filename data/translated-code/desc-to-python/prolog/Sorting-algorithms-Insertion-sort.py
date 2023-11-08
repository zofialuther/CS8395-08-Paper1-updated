```python
def insert_sort(L1):
    def insert_sort_intern(L1, L2):
        if L1 == []:
            return L2
        else:
            return insert_sort_intern(L1[1:], insert(L1[0], L2))
    
    def insert(elem, L):
        if L == []:
            return [elem]
        elif elem <= L[0]:
            return [elem] + L
        else:
            return [L[0]] + insert(elem, L[1:])
    
    return insert_sort_intern(L1, [])

```