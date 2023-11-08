def van_eck():
    n = 0
    seen = {}
    val = 0
    while True:
        yield val
        last = {val: n}
        val = n - seen.get(val, n)
        seen.update(last)
        n = n + 1

if __name__ == '__main__':
    from itertools import islice
    print("Van Eck: first 10 terms:  ", list(islice(van_eck(), 10)))
    print("Van Eck: terms 991 - 1000:", list(islice(van_eck(), 1000))[-10:])