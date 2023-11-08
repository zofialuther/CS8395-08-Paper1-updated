from sympy import factorint
from itertools import groupby
from operator import itemgetter

def proper_divisors(n):
    factors = factorint(n)
    divisors = [[key ** i for i in range(val + 1)] for key, val in factors.items()]
    return [int(x) for x in map(lambda y: y[0] * y[1], zip(*divisors))]

def f_table(s, x_show, fx_show, f, xs):
    w = max(map(lambda x: len(x_show(x)), xs))
    lines = '\n'.join([s] + [x_show(x).rjust(w) + ' -> ' + fx_show(f(x)) for x in xs])
    return lines

def main():
    print(f_table("Proper divisors of [1..10]:", str, str, proper_divisors, range(1, 11)))
    print("\nA number in the range 1 to 20,000 with the most proper divisors,\nas (number, count of proper divisors):\n")
    max_divisors = max(((i, len(proper_divisors(i))) for i in range(1, 20001)), key=itemgetter(1))
    print(max_divisors)

main()