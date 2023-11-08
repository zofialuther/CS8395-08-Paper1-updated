def subseq(list1, list2):
    return all(item in list2 for item in list1)

def maxsubseq(lst):
    subsequences = findall(lambda x: len(x) >= 1, maplist(lambda x: findall(lambda y: y in lst, x), findall(lambda z: len(z) >= 1, findall(lambda w: combinations(lst, w), length(lst)))))
    sums = maplist(lambda x: sum(x), subsequences)
    max_sum = max_list(sums)
    max_index = index(max_sum, sums)
    return nth(max_index, subsequences)