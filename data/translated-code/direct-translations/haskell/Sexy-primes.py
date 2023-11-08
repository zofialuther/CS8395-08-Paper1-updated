from Control.Lens import makeLenses, over, view, to
from Data.Numbers.Primes import isPrime, primes
from Text.Printf import printf

class Group:
    def __init__(self, count, results):
        self.count = count
        self.results = results

makeLenses(Group)

initialGroups = (Group(0, []), Group(0, []), Group(0, []), Group(0, []), Group(0, []))

def collect(r, n):
    pr, tt, qd, qn, un = r
    if isPrime(n-24) and isPrime(n-18) and isPrime(n-12) and isPrime(n-6):
        return (addPair(pr), addTriplet(tt), addQuad(qd), addQuin(qn), un)
    elif isPrime(n-18) and isPrime(n-12) and isPrime(n-6):
        return (addPair(pr), addTriplet(tt), addQuad(qd), qn, un)
    elif isPrime(n-12) and isPrime(n-6):
        return (addPair(pr), addTriplet(tt), qd, qn, un)
    elif isPrime(n-6):
        return (addPair(pr), tt, qd, qn, un)
    elif not isPrime(n+6) and not isPrime(n-6):
        return pr, tt, qd, qn, addUnSexy(un)
    else:
        return r

    n1 = n-6
    n2 = n-12
    n3 = n-18
    n4 = n-24

    addPair    = over(count, lambda x: x+1).over(results, lambda x: x[:5]+[(n1, n)])
    addTriplet = over(count, lambda x: x+1).over(results, lambda x: x[:5]+[(n2, n1, n)])
    addQuad    = over(count, lambda x: x+1).over(results, lambda x: x[:5]+[(n3, n2, n1, n)])
    addQuin    = over(count, lambda x: x+1).over(results, lambda x: x[:1]+[(n4, n3, n2, n1, n)])
    addUnSexy  = over(count, lambda x: x+1).over(results, lambda x: x[:10]+[n])

def main():
    pr, tt, qd, qn, un = collectGroups(primes)
    print("Number of sexy prime pairs: %d\n  Last 5 : %s\n\n" % (pr.count, display(pr.results)))
    print("Number of sexy prime triplets: %d\n  Last 5 : %s\n\n" % (tt.count, display(tt.results)))
    print("Number of sexy prime quadruplets: %d\n  Last 5 : %s\n\n" % (qd.count, display(qd.results)))
    print("Number of sexy prime quintuplets: %d\n  Last 1 : %s\n\n" % (qn.count, display(qn.results)))
    print("Number of unsexy primes: %d\n  Last 10: %s\n\n" % (un.count, display(un.results)))

def collectGroups(primes):
    return functools.reduce(collect, primes, initialGroups)

def display(results):
    return str(results[::-1])

if __name__ == "__main__":
    main()