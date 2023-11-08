class CatlanNumbers:
    def main(self):
        f1 = Catlan1()
        f2 = Catlan2()
        f3 = Catlan3()
        print("           Formula 1     Formula 2     Formula 3")
        for n in range(16):
            print(f1.catlin(n), f2.catlin(n), f3.catlin(n))

class Catlan:
    def catlin(self, n: int) -> int:
        pass

class Catlan1(Catlan):
    def catlin(self, n):
        numerator = []
        for k in range(n+2, 2*n+1):
            numerator.append(k)
        denominator = []
        for k in range(2, n):
            denominator.append(k)
        i = len(numerator) - 1
        while i >= 0:
            j = len(denominator) - 1
            while j >= 0:
                if denominator[j] == 1:
                    j -= 1
                    continue
                if numerator[i] % denominator[j] == 0:
                    val = numerator[i] // denominator[j]
                    numerator[i] = val
                    denominator.pop(j)
                    if val == 1:
                        break
                j -= 1
            i -= 1
        catlin = 1
        for i in range(len(numerator)):
            catlin *= numerator[i]
        for i in range(len(denominator)):
            catlin //= denominator[i]
        return catlin

class Catlan2(Catlan):
    CACHE = {0: 1}
    def catlin(self, n):
        if n in self.CACHE:
            return self.CACHE[n]
        catlin = 0
        n -= 1
        for i in range(n + 1):
            catlin += self.catlin(i) * self.catlin(n - i)
        self.CACHE[n+1] = catlin
        return catlin

class Catlan3(Catlan):
    CACHE = {0: 1}
    def catlin(self, n):
        if n in self.CACHE:
            return self.CACHE[n]
        catlin = 2 * (2 * n - 1) * self.catlin(n - 1) // (n + 1)
        self.CACHE[n] = catlin
        return catlin