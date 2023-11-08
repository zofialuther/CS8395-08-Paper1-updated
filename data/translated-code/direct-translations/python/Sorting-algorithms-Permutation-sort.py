import itertools
import more_itertools

def is_sorted(seq):
    return all(
        v1 <= v2
        for v1, v2 in more_itertools.windowed(seq, 2)
    )

def permutation_sort(seq):
    return next(
        permutation
        for permutation in itertools.permutations(seq)
        if is_sorted(permutation)
    )