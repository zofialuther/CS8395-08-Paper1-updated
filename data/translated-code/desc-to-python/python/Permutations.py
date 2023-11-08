def perm1(lst):
    def generate_permutations(k):
        if k == len(lst):
            yield tuple(lst)
        else:
            for i in range(k, len(lst)):
                lst[k], lst[i] = lst[i], lst[k]
                yield from generate_permutations(k + 1)
                lst[k], lst[i] = lst[i], lst[k]
    yield from generate_permutations(0)

def perm2(lst):
    def generate_permutations(k):
        if k == len(lst):
            yield tuple(lst)
        else:
            for i in range(k, len(lst)):
                lst[k], lst[i] = lst[i], lst[k]
                yield from generate_permutations(k + 1)
                lst[k:k+i+1] = lst[k:k+i+1][::-1]
    yield from generate_permutations(0)