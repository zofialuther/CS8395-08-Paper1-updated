from functools import lru_cache

@lru_cache(maxsize=4095)
def ld(s, t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if s[0] == t[0]:
        return ld(s[1:], t[1:])
    l1 = ld(s, t[1:])
    l2 = ld(s[1:], t)
    l3 = ld(s[1:], t[1:])
    return 1 + min(l1, l2, l3)

print(ld("kitten", "sitting"))
print(ld("rosettacode", "raisethysword"))