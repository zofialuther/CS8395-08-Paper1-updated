import cmath

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [0] * (N//2)
    for k in range(N//2):
        T[k] = cmath.exp(-2j * cmath.pi * k / N) * odd[k]
    result = [0] * N
    for k in range(N//2):
        result[k] = even[k] + T[k]
    for k in range(N//2):
        result[N//2 + k] = even[k] - T[k]
    return result

print(' '.join("%5.3f" % abs(f) for f in fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])))