from operator import itemgetter
import functools

def sorted(xs):
    maxLen = max([len(str(x)) for x in xs])
    def pad(x):
        return x + " " * ((maxLen - len(str(x))) + 1)
    return sorted(xs, key=functools.cmp_to_key(lambda x, y: (x > y) - (x < y)))

def maxcat(xs):
    return int("".join(sorted(map(str, xs))))

print(list(map(maxcat, [[1,34,3,98,9,76,45,4], [54,546,548,60]]))