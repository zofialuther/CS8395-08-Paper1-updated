def hammings():
    def merge(a, b):
        if not a:
            return b
        if not b:
            return a
        x, *xs = a
        y, *ys = b
        if x < y:
            return [x] + merge(xs, b)
        else:
            return [y] + merge(a, ys)
    
    r = [1]
    n = [2, 3, 5]
    for i in n:
        r = merge(r, [i * x for x in r])
    return r

def main():
    print(take 20(hammings()))
    print(hammings()[1690])
    print(hammings()[1000000 - 1])

if __name__ == "__main__":
    main()