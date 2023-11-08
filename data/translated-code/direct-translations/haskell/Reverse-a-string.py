def accumulatingReverse(lst):
    def rev(xs, a):
        return functools.reduce(lambda acc, x: [x] + acc, xs, a)
    
    return rev(lst, [])