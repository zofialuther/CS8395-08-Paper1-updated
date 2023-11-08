def moebius(integer):
    def m(tup):
        p, e = tup
        if unPrime(p) == 0:
            return 0
        elif e == 1:
            return -1
        else:
            return 0
    moebius = product(map(m, factorise))
    return moebius

def mertens(integer):
    mertens = Memo.integral(lambda n: sum(map(moebius, range(1, n+1)))
    return mertens

def countZeros(integers):
    countZeros = len(list(filter(lambda x: mertens(x) == 0, integers)))
    return countZeros

def crossesZero(integers):
    def go(integers):
        if integers:
            x, y, *xs = integers
            if y == 0 and x != 0:
                return [y] + go([y] + xs)
            else:
                return go([y] + xs)
        else:
            return []
    crossesZero = len(go(list(map(mertens, integers))))
    return crossesZero

def main():
    print("The first 99 terms for M(1..99):\n\n   ")
    list(map(lambda x: print(f"{mertens(x):3d}"), range(1, 10)))
    print("\n")
    chunks = [list(range(10*i, 10*(i+1))) for i in range(9)]
    list(map(lambda row: (list(map(lambda x: print(f"{mertens(x):3d}"), row)), print("\n")), chunks)
    print(f"M(n) is zero {countZeros(list(range(1, 1001)))} times for 1 <= n <= 1000.\n")
    print(f"M(n) crosses zero {crossesZero(list(range(1, 1001)))} times for 1 <= n <= 1000.\n")