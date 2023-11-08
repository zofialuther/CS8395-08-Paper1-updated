```python
import math
import random
import sys

class PierpontPrimes:
    def main(self):
        nf = NumberFormat()
        display("First 50 Pierpont primes of the first kind:", pierpontPrimes(50, True))
        display("First 50 Pierpont primes of the second kind:", pierpontPrimes(50, False))
        sys.stdout.write("The 250th Pierpont prime of the first kind is %d\n" % (pierpontPrimes(250, True).get(249)))
        sys.stdout.write("The 250th Pierpont prime of the second kind is %d\n" % (pierpontPrimes(250, False).get(249)))

    def display(self, message, primes):
        nf = NumberFormat()
        sys.stdout.write(message + "\n")
        for i in range(len(primes)):
            sys.stdout.write(nf.format(primes.get(i)))
            if (i + 1) % 10 == 0:
                sys.stdout.write("\n")

    def pierpontPrimes(self, n, first):
        primes = []
        if first:
            primes.append(2)
            n -= 1
        two = BigInt(2)
        twoTest = BigInt(3)
        three = BigInt(3)
        threeTest = BigInt(2)
        one = BigInt(1)
        mOne = BigInt(-1)
        twoIndex = 0
        threeIndex = 0
        twoSmooth = []
        count = 0
        while count < n:
            minTest = min(twoTest, threeTest)
            twoSmooth.append(minTest)
            if minTest == twoTest:
                twoTest = two.multiply(twoSmooth[twoIndex]).add(one)
                twoIndex += 1
            if minTest == threeTest:
                threeTest = three.multiply(twoSmooth[threeIndex]).add(mOne)
                threeIndex += 1
            test = 0
            if first:
                test = twoSmooth[count].modPow(two, three.multiply(2))
            else:
                test = twoSmooth[count].modPow(three, two.multiply(3))
            if test.isProbablePrime(10):
                primes.append(twoSmooth[count])
                count += 1
        return primes
```