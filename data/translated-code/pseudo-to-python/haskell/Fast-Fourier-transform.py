from cmath import exp, pi

def fft(xs):
    if not xs:
        return []
    elif len(xs) == 1:
        return xs
    else:
        n = len(xs)
        evens, odds = split(xs)
        ys = fft(evens)
        zs = fft(odds)
        ts = []
        for k in range(n):
            ts.append(exp_prime(zs[k], k, n))
        result = []
        for i in range(n):
            result.append(ys[i] + ts[i])
        return result

def split(xs):
    if len(xs) == 0:
        return ([], [])
    elif len(xs) == 1:
        return (xs, [])
    else:
        xt = []
        yt = []
        for i in range(len(xs)):
            if i % 2 == 0:
                xt.append(xs[i])
            else:
                yt.append(xs[i])
        return (xt, yt)

def exp_prime(z, k, n):
    return exp(-2 * pi * 1j * k / n) * z

def main():
    result = fft([1, 1, 1, 1, 0, 0, 0, 0])
    for i in range(len(result)):
        print(result[i])

main()