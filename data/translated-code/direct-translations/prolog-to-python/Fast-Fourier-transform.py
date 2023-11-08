```python
from math import cos, sin, pi

twiddles = {}

class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

def add(cx1, cx2):
    return ComplexNum(cx1.real + cx2.real, cx1.imag + cx2.imag)

def sub(cx1, cx2):
    return ComplexNum(cx1.real - cx2.real, cx1.imag - cx2.imag)

def mul(cx1, cx2):
    return ComplexNum(cx1.real * cx2.real - cx1.imag * cx2.imag, cx1.real * cx2.imag + cx2.real * cx1.imag)

def polar_cx(mag, theta):
    real = mag * cos(theta)
    imag = mag * sin(theta)
    return ComplexNum(real, imag)

def tw(t, cx):
    if t == 0:
        return ComplexNum(1, 0)
    elif t in twiddles:
        return twiddles[t]
    else:
        cx = polar_cx(1.0, -2 * pi * t)
        twiddles[t] = cx
        return cx

def fft_vals(N, even, odd):
    fft_vals_list = []
    for k in range(len(even)):
        tf = k / N
        cx = tw(tf, ComplexNum(0, 0))
        m = mul(cx, odd[k])
        v0 = add(even[k], m)
        v1 = sub(even[k], m)
        fft_vals_list.append([v0, v1])
    return fft_vals_list

def split(lst):
    lst0 = [x[0] for x in lst]
    lst1 = [x[1] for x in lst]
    return lst0, lst1

def fft(data):
    n = len(data)
    if n == 1:
        return data
    else:
        even = [data[i] for i in range(n) if i % 2 == 0]
        odd = [data[i] for i in range(1, n, 2)]
        even_fft = fft(even)
        odd_fft = fft(odd)
        fft_vals_list = fft_vals(n, even_fft, odd_fft)
        fft_vals_split = split(fft_vals_list)
        return fft_vals_split[0] + fft_vals_split[1]

def test():
    D = [ComplexNum(1, 0)] * 4 + [ComplexNum(0, 0)] * 4
    D_res = fft(D)
    print("fft =", end=" ")
    for cx in D_res:
        r = int(cx.real * 10**3) / 10**3
        i = int(cx.imag * 10**3) / 10**3
        print(f"{r}+{i}j", end=", ")
    print()

test()
```