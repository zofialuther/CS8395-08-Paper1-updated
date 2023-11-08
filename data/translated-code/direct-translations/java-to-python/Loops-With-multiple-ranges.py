```python
class LoopsWithMultipleRanges:
    sum = 0
    prod = 1

    def main(self):
        x = 5
        y = -5
        z = -2
        one = 1
        three = 3
        seven = 7

        jList = []
        for j in range(-three, pow(3, 3)+1, three):
            jList.append(j)
        for j in range(-seven, seven+1, x):
            jList.append(j)
        for j in range(555, 550-y+1, 1):
            jList.append(j)
        for j in range(22, -28-1, -three):
            jList.append(j)
        for j in range(1927, 1939+1, 1):
            jList.append(j)
        for j in range(x, y-1, z):
            jList.append(j)
        for j in range(pow(11, x), pow(11, x)+one+1, 1):
            jList.append(j)

        prodList = []
        for j in jList:
            self.sum += abs(j)
            if abs(self.prod) < pow(2, 27) and j != 0:
                prodList.append(j)
                self.prod *= j

        print(" sum        = {:,d}".format(self.sum))
        print("prod        = {:,d}".format(self.prod))
        print("j values    = {}".format(jList))
        print("prod values = {}".format(prodList))

    def pow(self, base, exponent):
        return int(base ** exponent)


LoopsWithMultipleRanges().main()
```