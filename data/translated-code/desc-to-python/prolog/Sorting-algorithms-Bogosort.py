def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
    return L

def is_sorted(L):
    return all(L[i] <= L[i+1] for i in range(len(L)-1))