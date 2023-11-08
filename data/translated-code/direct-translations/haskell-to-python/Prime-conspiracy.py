from itertools import groupby
import operator
import math

def freq(xs):
    return len(xs) / 100

def line(t):
    n1, n2 = t[0]
    print("%d -> %d count: %5d frequency: %2.2f %%" % (n1, n2, len(t), freq(t)))

def main():
    primes_list = list(primes())
    groups = [list(group) for key, group in groupby(sorted([(i % 10, i) for i in primes_list], key=operator.itemgetter(0)))]
    for group in groups[1:]:
        line(group)

main()