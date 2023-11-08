def rotate(Int, List):
    if isinstance(Int, int):
        Suff = List[-Int:]
        Pre = List[:-Int]
        Rotated = Suff + Pre
        return Rotated

def rotate_list(LoInts, LoLists):
    if isinstance(LoInts, list):
        Rotated = [rotate(int_val, list_val) for int_val, list_val in zip(LoInts, LoLists)]
        return Rotated

def append_(Suff, Pre, List):
    return Pre + Suff + List

def idmatrix(N):
    ones = [1] * N
    zeros = [0] * (N-1)
    M = ones + zeros
    Offsets = list(range(N-1))
    IdMatrix = [rotate(offset, M) for offset in Offsets]
    return IdMatrix

def main():
    I = idmatrix(5)
    for row in I:
        print(row)