def rosetta_sort():
    L = ["Here", "are", "some", "sample", "strings", "to", "be", "sorted"]
    L1 = sorted(L, key=my_comp)
    print('Input list:')
    for word in L:
        print(word, end=' ')
    print('\n')
    print('Sorted list:')
    for word in L1:
        print(word, end=' ')

def my_comp(w1, w2):
    if len(w1) < len(w2):
        return -1
    elif len(w1) > len(w2):
        return 1
    else:
        return 0 if w1 == w2 else -1 if w1 < w2 else 1

rosetta_sort()