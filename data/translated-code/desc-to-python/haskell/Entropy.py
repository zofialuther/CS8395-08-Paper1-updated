from math import log2
from collections import Counter

def entropy(s):
    p, lns = Counter(s), float(len(s))
    return -sum( count/lns * log2(count/lns) for count in p.values())

def main():
    s = "1223334444"
    print(entropy(s))

if __name__ == "__main__":
    main()