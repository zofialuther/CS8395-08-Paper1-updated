from math import BigInteger

class Pi:
    def __init__(self):
        self.TWO = BigInteger(2)
        self.THREE = BigInteger(3)
        self.FOUR = BigInteger(4)
        self.SEVEN = BigInteger(7)
        self.q = BigInteger(1)
        self.r = BigInteger(0)
        self.t = BigInteger(1)
        self.k = BigInteger(1)
        self.n = BigInteger(3)
        self.l = BigInteger(3)

    def calcPiDigits(self):
        nn = BigInteger(0)
        nr = BigInteger(0)
        first = True
        while True:
            if self.FOUR.multiply(self.q).add(self.r).subtract(self.t).compare_to(self.n.multiply(self.t)) == -1:
                print(self.n)
                if first:
                    print(".")
                    first = False
                nr = BigInteger.TEN.multiply(self.r.subtract(self.n.multiply(self.t)))
                self.n = BigInteger.TEN.multiply(self.THREE.multiply(self.q).add(self.r)).divide(self.t).subtract(BigInteger.TEN.multiply(self.n))
                self.q = self.q.multiply(BigInteger.TEN)
                self.r = nr
            else:
                nr = self.TWO.multiply(self.q).add(self.r).multiply(self.l)
                nn = self.q.multiply((self.SEVEN.multiply(self.k))).add(self.TWO).add(self.r.multiply(self.l)).divide(self.t.multiply(self.l))
                self.q = self.q.multiply(self.k)
                self.t = self.t.multiply(self.l)
                self.l = self.l.add(BigInteger(2))
                self.k = self.k.add(BigInteger(1)
                self.n = nn
                self.r = nr

    def main(self):
        p = Pi()
        p.calcPiDigits()