from itertools import zip_longest
from sympy import primerange

def is_brilliant(n):
    factors = list(primerange(n))
    if len(factors) == 2:
        if len(str(factors[0])) == len(str(factors[1])):
            return True
    return False

indexed_brilliants = list(enumerate(filter(is_brilliant, range(1, 101))))

def display_table(rows):
    table = zip_longest(*rows, fillvalue='')
    col_widths = [max(len(str(x)) for x in col) for col in table]
    for row in rows:
        print('  '.join(str(x).ljust(col_widths[i]) for i, x in enumerate(row)))

def display_index_brilliant(indexed_brilliants):
    display_table(indexed_brilliants[:100])
    print("(index, brilliant)")
    for i in range(5):
        print(indexed_brilliants[i][0])

display_index_brilliant(indexed_brilliants)