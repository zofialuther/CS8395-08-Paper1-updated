```python
def rotate(Int, List):
    rotated = List[Int:] + List[:Int]
    return rotated

def rotate_lists(LoInts, LoLists):
    rotated = [rotate(ints, lst) for ints, lst in zip(LoInts, LoLists)]
    return rotated

def append_(Suff, Pre, List):
    return [Pre] + Suff + List

def idmatrix(N):
    ones = [1] * N
    zeros = [0] * (N-1)
    m = [append_(zeros, ones, [0]) for _ in range(N)]
    offsets = list(range(N))
    id_matrix = rotate(offsets, m)
    return id_matrix

def main():
    I = idmatrix(5)
    for row in I:
        print(row)

main()
```