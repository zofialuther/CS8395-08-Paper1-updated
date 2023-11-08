def posd():
    count = 1
    odd = 3
    while True:
        yield count
        yield odd
        count = count + 1
        odd = odd + 2

def pos_gen():
    val = 1
    diff = posd()
    while True:
        yield val
        val = val + next(diff)

def plus_minus():
    n = 0
    sign = [1, 1]
    p_gen = pos_gen()
    out_on = next(p_gen)
    while True:
        n = n + 1
        if n == out_on:
            next_sign = sign.pop(0)
            if not sign:
                sign = [-next_sign, -next_sign]
            yield -n, next_sign
            out_on = next(p_gen)
        else:
            yield 0

def part(n):
    p = [1]
    p_m = plus_minus()
    mods = []
    for _ in range(n):
        next_plus_minus = next(p_m)
        if next_plus_minus:
            mods.append(next_plus_minus)
        p.append(sum(p[offset] * sign for offset, sign in mods))
    return p[-1]

print("(Intermediaries):")
print("    posd:", list(islice(posd(), 10)))
print("    pos_gen:", list(islice(pos_gen(), 10)))
print("    plus_minus:", list(islice(plus_minus(), 15))
print("\nPartitions:", [part(x) for x in range(15)])