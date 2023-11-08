def scanl(f, acc, xs):
    result = [acc]
    for x in xs:
        acc = f(acc, x)
        result.append(acc)
    return result

def main():
    leftFact = scanl(add, 0, fact())
    print("0 ~ 10:")
    for i in range(11):
        print(leftFact[i])
    print("")
    print("20 ~ 110 by tens:")
    for i in range(20, 111, 10):
        print(leftFact[i])
    print("")
    print("length of 1,000 ~ 10,000 by thousands:")
    for i in range(1000, 11001, 1000):
        print(len(str(leftFact[i])))
    print("")

def fact():
    result = scanl(multiply, 1, range(1, 100000))
    return result