from itertools import accumulate, chain

def subseqs(lst):
    return [list(accumulate(sub)) for sub in chain.from_iterable([lst[i:] for i in range(len(lst))])]

def maxsubseq(lst):
    return max(subseqs(lst), key=sum)

print(maxsubseq([-1, -2, 3, 5, 6, -2, -1, 4, -4, 2, -1]))