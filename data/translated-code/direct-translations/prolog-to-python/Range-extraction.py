```python
from typing import List

def range_extract() -> None:
    L = [0, 1, 2, 4, 6, 7, 8, 11, 12, 14,
         15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
         25, 27, 28, 29, 30, 31, 32, 33, 35, 36,
         37, 38, 39]
    print(L)
    LP = pack_Range(L)
    R = [study_Range(r) for r in LP]
    LA = extract_Range(L, R)
    A = ''.join(map(str, LA))
    print(A)

def extract_Range(X: List[int], R: List[List[int]]) -> List[List[int]]:
    if not X:
        return []
    else:
        Range, X1 = get_Range(X, [], [])
        return [Range] + extract_Range(X1, R)

def get_Range(X: List[int], Range: List[int], R: List[int]) -> List[int]:
    if not X:
        return Range, []
    elif X[0] == ',':
        return Range, X[1:]
    else:
        return get_Range(X[1:], Range + [X[0]], R)

def study_Range(Range1: List[int]) -> List[int]:
    if len(Range1) == 1:
        return [Range1[0], Range1[0]]
    else:
        Deb = int(''.join(map(str, Range1[:Range1.index('-')]))
        Fin = int(''.join(map(str, Range1[Range1.index('-')+1:]))
        return [Deb, Fin]

def pack_Range(L: List[int]) -> List[List[List[int]]]:
    if not L:
        return []
    else:
        V = [L[0]]
        for i in range(1, len(L)):
            if L[i] != V[-1] and L[i] != V[-1] + 1:
                return [V] + pack_Range(L[i:])
            else:
                V.append(L[i])
        return [V]

range_extract()
```