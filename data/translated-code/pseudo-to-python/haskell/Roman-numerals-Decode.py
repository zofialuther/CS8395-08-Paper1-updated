def tr(s, kv):
    k, v = kv
    while s.startswith(k):
        s = (s[len(k):], v + s)
    return s

def romanValue(s):
    trList = [ ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1) ]
    total = 0
    for pair in trList:
        total += sum(mapAccumL(tr, s, pair)[1])
    return total

def main():
    inputs = [ "MDCLXVI", "MCMXC", "MMVIII", "MMXVI", "MMXVII" ]
    for input in inputs:
        print(romanValue(input))

main()