```python
from itertools import permutations, chain

def main():
    print(report(
        concatMap(dinesman)(
            permutations(range(1, 6))
        )
    ))

def dinesman(bcfms):
    [b, c, f, m, s] = bcfms
    if all([
        5 != b,
        1 != c,
        1 != f,
        5 != f,
        c < m,
        1 < abs(s - f),
        1 < abs(c - f)
    ]):
        return [bcfms]
    else:
        return []

def report(xs):
    if xs:
        return ', '.join(list(map(
            lambda k, n: k + ' in ' + str(n),
            ['Baker', 'Cooper', 'Fletcher', 'Miller', 'Smith'],
            xs[0]
        ))) + '.'
    else:
        return 'No solution found.'

def concatMap(f, xs):
    return list(
        chain.from_iterable(map(f, xs))
    )

if __name__ == '__main__':
    main()
```