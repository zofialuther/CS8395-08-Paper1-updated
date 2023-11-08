numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romannumeral2number(roman):
    from functools import reduce
    return reduce(lambda total, i: total + numerals[i] if numerals[i] >= numerals.get(roman[roman.index(i) + 1], 0) else total - numerals[i], roman, 0)