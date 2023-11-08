from math import cos, sin, log, pi

class Complex:
    def __init__(self, r=0, i=0):
        self.re = r
        self.im = i

    def add(self, b):
        return Complex(self.re + b.re, self.im + b.im)

    def sub(self, b):
        return Complex(self.re - b.re, self.im - b.im)

    def mult(self, b):
        return Complex(self.re * b.re - self.im * b.im, self.re * b.im + self.im * b.re)

    def __str__(self):
        return f"({self.re},{self.im})"

def bitReverse(n, bits):
    reversedN = n
    count = bits - 1
    n >>= 1
    while n > 0:
        reversedN = (reversedN << 1) | (n & 1)
        count -= 1
        n >>= 1
    return ((reversedN << count) & ((1 << bits) - 1))

def fft(buffer):
    bits = int(log(len(buffer)) / log(2))
    for j in range(1, len(buffer) // 2):
        swapPos = bitReverse(j, bits)
        temp = buffer[j]
        buffer[j] = buffer[swapPos]
        buffer[swapPos] = temp

    for N in range(2, len(buffer) + 1):
        i = 0
        while i < len(buffer):
            k = 0
            while k < N / 2:
                evenIndex = i + k
                oddIndex = i + k + (N // 2)
                even = buffer[evenIndex]
                odd = buffer[oddIndex]
                term = (-2 * pi * k) / N
                exp = Complex(cos(term), sin(term)).mult(odd)
                buffer[evenIndex] = even.add(exp)
                buffer[oddIndex] = even.sub(exp)
                k += 1
            i += N

def main():
    input = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    cinput = [Complex(x, 0.0) for x in input]
    fft(cinput)
    print("Results:")
    for c in cinput:
        print(c)

if __name__ == "__main__":
    main()