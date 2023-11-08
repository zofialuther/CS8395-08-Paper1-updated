import itertools

def is_solution(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if abs(i - j) == abs(perm[i] - perm[j]):
                return False
    return True

for perm in itertools.permutations(range(8)):
    if is_solution(perm):
        print(perm)