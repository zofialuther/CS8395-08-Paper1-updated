```python
import math

class FastFourierTransform:
    
    @staticmethod
    def bit_reverse(n, bits):
        reversed_n = n
        count = bits - 1
        n >>= 1
        while n > 0:
            reversed_n = (reversed_n << 1) | (n & 1)
            count -= 1
            n >>= 1
        return ((reversed_n << count) & ((1 << bits) - 1))

    @staticmethod
    def fft(buffer):
        bits = int(math.log(len(buffer)) / math.log(2))
        for j in range(1, len(buffer) // 2):
            swap_pos = FastFourierTransform.bit_reverse(j, bits)
            temp = buffer[j]
            buffer[j] = buffer[swap_pos]
            buffer[swap_pos] = temp

        for N in range(2, len(buffer) + 1):
            i = 0
            while i < len(buffer):
                for k in range(0, N // 2):
                    even_index = i + k
                    odd_index = i + k + (N // 2)
                    even = buffer[even_index]
                    odd = buffer[odd_index]
                    term = (-2 * math.pi * k) / float(N)
                    exp = Complex(math.cos(term), math.sin(term)).mult(odd)
                    buffer[even_index] = even.add(exp)
                    buffer[odd_index] = even.sub(exp)
                i += N

    @staticmethod
    def main():
        input_array = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
        cinput = [Complex(x, 0.0) for x in input_array]
        FastFourierTransform.fft(cinput)
        print("Results:")
        for c in cinput:
            print(c)

class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def add(self, b):
        return Complex(self.re + b.re, self.im + b.im)

    def sub(self, b):
        return Complex(self.re - b.re, self.im - b.im)

    def mult(self, b):
        return Complex(self.re * b.re - self.im * b.im, self.re * b.im + self.im * b.re)

    def __str__(self):
        return f"({self.re},{self.im})"

FastFourierTransform.main()
```