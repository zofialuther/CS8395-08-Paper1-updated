numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romannumeral2number(s):
    s = s.upper()
    values = list(map(lambda x: numerals[x], s))
    result = 0
    for i in range(len(values)-1):
        if values[i] < values[i+1]:
            result -= values[i]
        else:
            result += values[i]
    result += values[-1]
    return result