from itertools import groupby
import operator
import math

def freq(xs):
    return len(xs) / 100

def line(t):
    n1, n2 = t[0]
    print(f"{n1} -> {n2} count: {len(t):>5} frequency: {freq(t):.2f} %")

def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # Example list of primes
    groups = [list(group) for key, group in groupby(sorted([(0, n) for n in primes], key=operator.itemgetter(1)), key=operator.itemgetter(0))]
    map(line, groups)

main()