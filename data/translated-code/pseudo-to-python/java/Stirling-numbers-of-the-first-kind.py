class SterlingNumbersFirstKind:
    def main(self):
        print("Unsigned Stirling numbers of the first kind:")
        max = 12
        print("n/k")
        for n in range(0, max+1):
            print(n)
            for k in range(0, max+1):
                print(k)

    def sterling1(self, n, k):
        if (n, k) in COMPUTED:
            return COMPUTED[(n, k)]
        if n == 0 and k == 0:
            return 1
        if n > 0 and k == 0:
            return 0
        if k > n:
            return 0
        result = # calculate using the formula
        COMPUTED[(n, k)] = result
        return result

    COMPUTED = {}
    previous = 0
    for k in range(1, 101):
        current = sterling1(5, k)
        if current > previous:
            previous = current
        else:
            print(previous, len(str(previous)))
            break