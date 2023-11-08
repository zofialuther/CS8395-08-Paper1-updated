from math import sqrt

def qmean(num):
    return sqrt(sum(n*n for n in num)/len(num))

print(qmean(range(1,11)))