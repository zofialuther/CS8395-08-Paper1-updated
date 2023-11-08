def permutations(lst):
    if len(lst) == 0:
        return [[]]
    else:
        res = []
        for perm in permutations(lst[1:]):
            for i in range(len(lst)):
                res.append(perm[:i] + [lst[0]] + perm[i:])
        return res

def main():
    result = permutations([1, 2, 3])
    print(result)

main()