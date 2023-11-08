def expand(p):
    z = 1
    for i in range(1, p+1):
        z = z * (p - i + 1) // i
        print(z)

def test(p):
    if p < 2:
        return False
    else:
        for n in expand(p):
            if n % p == 0:
                return True
            else:
                return False

def printPoly(p):
    if p == [1]:
        print("1")
    else:
        l = len(p)
        for i in range(l-1, 0, -1):
            if i % 2 == 0:
                sgn = "+"
            else:
                sgn = "-"
            pow = str(i) + "x^" + (str(i) if i > 1 else "")
            print(pow, sgn, p[i-1])

def main():
    print("-- p: (x-1)^p for small p")
    for i in range(11):
        print(str(i) + ": " + str(expand(i)))
    print("-- Primes up to 100:")
    print(list(filter(test, list(range(1, 101)))) )