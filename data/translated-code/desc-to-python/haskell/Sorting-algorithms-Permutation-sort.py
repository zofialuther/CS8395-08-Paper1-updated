def permutationSort(input_list):
    from itertools import permutations
    
    def permute(lst):
        result = [[]]
        for x in lst:
            new_perm = []
            for perm in result:
                for i in range(len(perm)+1):
                    new_perm.append(perm[:i] + [x] + perm[i:])
            result = new_perm
        return result
    
    for perm in permutations(input_list):
        if sorted(perm) == list(perm):
            return list(perm)