```python
from urllib.request import urlopen
from itertools import groupby
from operator import itemgetter

def longest_deranged_anagram():
    with urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt') as In:
        Out = [line.decode('utf-8').strip() for line in In]

    MOut = sorted(Out)
    GPL = groupby(MOut, len)
    NGPL = [(key, list(group)) for key, group in GPL]
    GPLSort = sorted(NGPL, key=itemgetter(0))
    search_derangement(GPLSort)

def my_compare(N1, (K1, E1), N2, (K2, E2)):
    if N1 < N2:
        return 1
    elif N1 > N2:
        return -1
    else:
        L1 = len(E1)
        L2 = len(E2)
        if L1 < L2:
            return -1
        elif L1 > L2:
            return 1
        else:
            return (K1 > K2) - (K1 < K2)

def compute_len(_, (H, _)):
    return len(H)

def derangement(T1, T2):
    if not T1 and not T2:
        return True
    elif T1 and T2:
        H1, *T1_rest = T1
        H2, *T2_rest = T2
        if H1 != H2:
            return derangement(T1_rest, T2_rest)
    return False

def search_derangement(T):
    for _, (_, L) in T:
        if len(L) == 1:
            continue
        else:
            if not search(L):
                search_derangement(T)

def search(L):
    for H in L:
        if search_one(H, L):
            return True
    return False

def search_one(Word, L):
    for H in L:
        if derangement(Word, H):
            print(f'Longest deranged anagrams: {Word} {H}')
            return True
    return False

def read_file(In, L, L1):
    W = In.readline().decode('utf-8').strip()
    if W == "":
        L1 = L
    else:
        W1 = ''.join(sorted(W))
        L.append((W1, W))
        L1 = read_file(In, L, L1)
    return L1

longest_deranged_anagram()
```