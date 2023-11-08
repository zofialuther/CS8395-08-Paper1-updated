from math import sqrt, floor
from java.math import BigInteger
from java.text import NumberFormat
from java.util import ArrayList

class PellsEquation:
    def main(self):
        format = NumberFormat.getInstance()
        for n in [61, 109, 181, 277, 8941]:
            pell = self.pellsEquation(n)
            print("x^2 - " + str(n) + " * y^2 = 1 for:")
            print("    x = " + format(pell[0]))
            print("    y = " + format(pell[1]))

    def pellsEquation(self, n):
        a0 = sqrt(n)
        if a0 * a0 == n:
            raise ValueError("ERROR 102:  Invalid n = " + str(n))
        continuedFrac = self.continuedFraction(n)
        count = 0
        ajm2 = 1
        ajm1 = BigInteger(str(a0))
        bjm2 = 0
        bjm1 = 1
        stop = (len(continuedFrac) % 2 == 1)
        if len(continuedFrac) == 2:
            stop = True
        while True:
            count += 1
            bn = BigInteger(str(continuedFrac[count]))
            aj = bn.multiply(ajm1).add(ajm2)
            bj = bn.multiply(bjm1).add(bjm2)
            if stop and (count == len(continuedFrac) - 2 or len(continuedFrac) == 2):
                return [aj, bj]
            elif len(continuedFrac) % 2 == 0 and count == len(continuedFrac) - 2:
                stop = True
            if count == len(continuedFrac) - 1:
                count = 0
            ajm2 = ajm1
            ajm1 = aj
            bjm2 = bjm1
            bjm1 = bj

    def continuedFraction(self, n):
        answer = ArrayList()
        a0 = sqrt(n)
        answer.add(a0)
        a = -a0
        aStart = a
        b = 1
        bStart = b
        while True:
            values = self.iterateFrac(n, a, b)
            answer.add(values[0])
            a = values[1]
            b = values[2]
            if a == aStart and b == bStart:
                break

    def iterateFrac(self, n, a, b):
        x = floor((b * sqrt(n) - b * a) / (n - a * a))
        answer = [0, 0, 0]
        answer[0] = x
        answer[1] = -(b * a + x * (n - a * a)) / b
        answer[2] = (n - a * a) / b
        return answer