from itertools import accumulate

def fact(n):
    return accumulate(range(1, n+1), lambda x, y: x*y)

def leftFact(n):
    return accumulate(fact(n), lambda x, y: x+y)

def main():
    print(list(leftFact(11)))
    print(list(leftFact(i) for i in range(20, 111, 10)))
    print(len(list(leftFact(i) for i in range(1000, 10001, 1000)))

main()