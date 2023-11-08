```python
def lcm(x, y):
    return lambda y: 0 if 0 in (x, y) else abs(y * (x // gcd_(x)(y)))

def gcd_(x):
    return lambda y: 
        def go(a, b):
            if b != 0:
                return go(b, a % b)
            else:
                return a
        return go(abs(x), abs(y))

def main():
    print(fTable(__doc__ + 's of 60 and [12..20]:')(repr)(repr)(lcm(60))(enumFromTo(12)(20)))
    pairs = [(0, 2), (2, 0), (-6, 14), (12, 18)]
    print(fTable('\n\n' + __doc__ + 's of ' + repr(pairs) + ':')(repr)(repr)(uncurry(lcm))(pairs))

def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))

def uncurry(f):
    if len(signature(f).parameters) > 1:
        return lambda xy: f(*xy)
    else:
        return lambda xy: f(xy[0])(xy[1])

def unlines(xs):
    return '\n'.join(xs)

def fTable(s):
    return lambda xShow: 
        return lambda fxShow: 
            return lambda f: 
                return lambda xs: 
                    def go(xShow, fxShow, f, xs):
                        ys = [xShow(x) for x in xs]
                        w = max(map(len, ys))
                        return s + '\n' + '\n'.join(map(
                            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
                            xs, ys
                        ))
                    return go(xShow, fxShow, f, xs)

if __name__ == '__main__':
    main()
```