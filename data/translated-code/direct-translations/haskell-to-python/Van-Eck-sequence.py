from functools import reduce
import operator

# VAN ECK SEQUENCE
def van_eck():
    seq = [0]
    dct = {}
    for i in range(1, 1000000):
        x = seq[-1]
        if x not in dct:
            seq.append(0)
            dct[x] = i
        else:
            seq.append(i - dct[x])
            dct[x] = i
    return seq

# TEST
def main():
    seq = van_eck()
    for n in [10, 1000, 10000, 100000, 1000000]:
        print(seq[n-10:n])

main()