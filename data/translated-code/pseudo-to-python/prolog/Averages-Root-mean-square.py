def main():
    Xs = []
    for i in range(1, 11):
        Xs.append(i)
    Y = rms(Xs)
    print("The root-mean-square of 1..10 is " + str(Y))

def rms(Xs):
    Sum = 0
    for X in Xs:
        Sum += X * X
    N = length(Xs)
    Y = (Sum / N) ** 0.5
    return Y

def length(Xs):
    count = 0
    for _ in Xs:
        count += 1
    return count

main()