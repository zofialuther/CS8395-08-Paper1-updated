def allEq(lst):
    return until(lambda x: len(set(x)) == 1, lambda x: x)(lst)

def allInc(lst):
    return until(lambda x: all(x[i] <= x[i+1] for i in range(len(x)-1)), lambda x: x)(lst)