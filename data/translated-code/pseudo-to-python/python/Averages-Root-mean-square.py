from math import sqrt

def qmean(num):
    mean = sum(x**2 for x in num) / len(num)
    result = sqrt(mean)
    return result

print(qmean(range(1,11)))