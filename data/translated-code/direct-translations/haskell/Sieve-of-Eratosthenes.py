def primes():
    def _Y(g):
        return g(lambda: _Y(g))
    
    def gaps(k, s):
        if k < s[0]:
            return [k] + gaps(k+2, s)
        else:
            return gaps(k+2, s[1:])
    
    def _U(t):
        if len(t) == 0:
            return []
        else:
            x, xs = t[0]
            return [x] + merge(xs, _U(pairs(t[1:])))
    
    def pairs(t):
        if len(t) < 2:
            return []
        else:
            xs, ys = t[0], t[1]
            return [merge(xs, ys)] + pairs(t[2:])
    
    def merge(xs, ys):
        if len(xs) == 0:
            return ys
        elif len(ys) == 0:
            return xs
        else:
            x, xt = xs[0], xs[1:]
            y, yt = ys[0], ys[1:]
            if x < y:
                return [x] + merge(xt, ys)
            elif y < x:
                return [y] + merge(xs, yt)
            else:
                return [x] + merge(xt, yt)
    
    def generate_primes():
        n = 3
        while True:
            yield n
            n += 2
    
    prime_generator = generate_primes()
    
    def sieve():
        while True:
            prime = next(prime_generator)
            yield prime
            yield from (i for i in range(prime*prime, 10**10, prime+prime))
    
    return [2] + _Y(lambda x: [next(sieve())] + x)

# Test the function
print(primes())