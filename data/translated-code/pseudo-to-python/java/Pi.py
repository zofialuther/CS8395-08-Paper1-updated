from math import BigInteger

class Pi:
    TWO = BigInteger(2)
    THREE = BigInteger(3)
    FOUR = BigInteger(4)
    SEVEN = BigInteger(7)
    
    q = BigInteger(1)
    r = BigInteger(0)
    t = BigInteger(1)
    k = BigInteger(1)
    n = BigInteger(3)
    l = BigInteger(3)
    
    def calcPiDigits(self):
        nn = 0
        nr = 0
        first = True
        while True:
            if self.FOUR.multiply(self.q).add(self.r).subtract(self.t).compare_to(self.n.multiply(self.t)) == -1:
                print(self.n)
                if first:
                    print(".")
                    first = False
                nr = 10 * (self.r - self.n.multiply(self.t))
                self.n = 10 * (3 * self.q + self.r) // self.t - 10 * self.n
                self.q = self.q * 10
                self.r = nr
                # FLUSH output
            else:
                nr = 2 * self.q + self.r * self.l
                nn = self.q * (7 * self.k) + 2 + self.r * self.l // (self.t * self.l)
                self.q = self.q * self.k
                self.t = self.t * self.l
                self.l = self.l + 2
                self.k = self.k + 1
                self.n = nn
                self.r = nr
                
    def main(self):
        p = Pi()
        p.calcPiDigits()