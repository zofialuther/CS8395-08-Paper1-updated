from itertools import accumulate, chain, count, islice
from operator import mul, add


def leftFact():
    '''Left factorial series defined in terms
       of the factorial series.
    '''
    return accumulate(chain([0], fact()), add)


def fact():
    '''The factorial series.
    '''
    return accumulate(chain([1], count(1)), mul)


def main():
    '''Tests'''
    print(
        'Terms 0 thru 10 inclusive:\n  %r'
        % list(islice(leftFact(), 11))
    )

    print('\nTerms 20 thru 110 (inclusive) by tens:')
    for x in islice(leftFact(), 20, 111, 10):
        print(x)

    print(
        '\n\nDigit counts for terms 1k through 10k (inclusive) by k:\n  %r'
        % list(map(
            lambda x: len(str(x)),
            islice(leftFact(), 1000, 10001, 1000)
        ))
    )


def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


def scanl(f):
    '''scanl is like reduce, but defines a succession of
       intermediate values, building from the left.
    '''
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go


def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


def takeFromThenTo(a):
    '''Values drawn from a series betweens positions a and b
       at intervals of size z'''
    return lambda b: lambda z: lambda xs: islice(
        xs, a, 1 + z, b - a
    )


if __name__ == '__main__':
    main()