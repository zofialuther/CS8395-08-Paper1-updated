def bell_tri():
    def f(xs):
        return (xs[-1], xs)
    return list(map(lambda x: x[1], iterate(lambda x: f(uncurry(lambda a, b: scanl(lambda c, d: c + d), x)), (1, [1]))))

bell_tri = bell_tri()

def bell():
    return list(map(lambda x: x[0], bell_tri))

bell = bell()

def main():
    print("First 10 rows of Bell's Triangle:")
    list(map(lambda x: print(x), bell_tri[:10]))
    print("\nFirst 15 Bell numbers:")
    list(map(lambda x: print(x), bell[:15]))
    print("\n50th Bell number:")
    print(bell[49])

main()