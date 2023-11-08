from cmath import exp, pi, cis

def fft(xs):
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return xs
    else:
        n = len(xs)
        evens, odds = split(xs)
        ys = fft(evens)
        zs = fft(odds)
        ts = [exp'((k * cis(-2 * pi * k) / n), n) for k in range(len(zs))]
        return [ys[i] + ts[i] for i in range(len(ys))] + [ys[i] - ts[i] for i in range(len(ys))]

def split(xs):
    evens = xs[::2]
    odds = xs[1::2]
    return evens, odds

def exp'(z, n):
    return z

if __name__ == "__main__":
    result = fft([1, 1, 1, 1, 0, 0, 0, 0])
    for item in result:
        print(item)