class AksTest:
    c = [0]*64

    def main(self):
        for n in range(0, 11):
            self.coeff(n)
            self.show(n)

        print("Primes:")
        for n in range(len(self.c)):
            if self.isPrime(n):
                print(n)
        print("\n")

    def coeff(self, n):
        self.c[0] = 1
        for i in range(0, n):
            self.c[0] = -self.c[0]
            for j in range(i, 0, -1):
                self.c[j] = self.c[j - 1] - self.c[j]

    def isPrime(self, n):
        self.coeff(n)
        self.c[0] += 1
        self.c[n] -= 1

        i = n
        while i != 0 and self.c[i] % n == 0:
            pass
        return i < 0

    def show(self, n):
        print("(x-1)^" + str(n) + " =")
        for i in range(n, -1, -1):
            print(" + " + str(self.c[i]) + "x^" + str(i))
        print("\n")