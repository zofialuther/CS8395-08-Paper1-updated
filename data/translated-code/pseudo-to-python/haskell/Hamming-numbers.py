def hammings():
    s = [1]
    prime_factors = [2, 3, 5]
    
    def merge(a, b):
        if not a:
            return b
        if not b:
            return a
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])
            
    for n in prime_factors:
        r = merge(s, [i * n for i in s])
        s = r[:]

    return r[:20]

def main():
    print(hammings()[:20])
    print(hammings()[1690])
    print(hammings()[999999])