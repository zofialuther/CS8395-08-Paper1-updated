def rosetta_sort():
    L = ["Here", "are", "some", "sample", "strings", "to", "be", "sorted" ]
    L1 = sorted(L, key=my_comp)
    print('Input list :')
    for word in L:
        my_write(word)
    print('\n')
    print('Sorted list :')
    for word in L1:
        my_write(word)

def my_comp(W):
    return len(W)

def my_write(W):
    print(W, end=' ')