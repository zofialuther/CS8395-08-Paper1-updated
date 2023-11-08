import itertools

n = 8
cols = range(n)

for vec in itertools.permutations(cols):
    sum1 = set(vec[i] + i for i in cols)
    sum2 = set(vec[i] - i for i in cols)
    
    if n == len(sum1) == len(sum2):
        print(vec)