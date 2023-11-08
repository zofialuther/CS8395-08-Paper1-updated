leftFact = list(itertools.accumulate(fact, operator.add, initial=0))

fact = itertools.accumulate(range(1, 100000), operator.mul, initial=1)

def main():
    print("0 ~ 10:")
    for i in range(11):
        print(leftFact[i])
    print("")
    print("20 ~ 110 by tens:")
    for i in range(20, 111, 10):
        print(leftFact[i])
    print("")
    print("length of 1,000 ~ 10,000 by thousands:")
    for i in range(1000, 10001, 1000):
        print(len(str(leftFact[i])))
    print("")

main()