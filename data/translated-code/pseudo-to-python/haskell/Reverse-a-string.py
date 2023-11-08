def accumulatingReverse(lst):
    def rev(xs, a):
        return foldl(lambda acc, x: x + acc, a, xs)
    return rev(lst, [])