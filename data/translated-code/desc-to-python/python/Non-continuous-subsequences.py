import sys
import psyco

psyco.full()

def C(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return C(n-1, k-1) + C(n-1, k)

nsubs = lambda s: 2**len(s) - 1

def ncsub(seq):
    result = []
    for i in range(len(seq)):
        for j in range(i+1, len(seq)+1):
            result.append(seq[i:j])
    return result

if __name__ == "__main__":
    input_size = int(sys.argv[1])
    seq = list(range(input_size))
    subsets = ncsub(seq)
    print(len(subsets))