def comb(n, iterable):
    combinations = []
    for i in range(len(iterable)):
        for j in range(i+1, len(iterable)):
            for k in range(j+1, len(iterable)):
                combination = [iterable[i], iterable[j], iterable[k]]
                combinations.append(combination)
    return combinations

print(comb(3, range(5)))