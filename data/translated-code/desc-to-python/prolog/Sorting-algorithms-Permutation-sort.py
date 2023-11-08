def permutation_sort(L):
    permutations = permutation(L)
    sorted_permutations = [perm for perm in permutations if sorted(perm) == perm]
    return sorted_permutations[0]

def sorted(L):
    return all(L[i] <= L[i+1] for i in range(len(L)-1))

def permutation(L):
    if len(L) == 0:
        return [[]]
    else:
        result = []
        for i in range(len(L)):
            smaller_permutations = permutation(L[:i] + L[i+1:])
            for perm in smaller_permutations:
                result.append([L[i]] + perm)
        return result