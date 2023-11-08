from typing import Set
import collections

a: Set[int] = {1, 2, 3, 4, 5}
b: Set[int] = {2, 3, 4, 5, 6, 8}
c: Set[int] = {2, 3, 4}
d: Set[int] = {2, 3, 4}

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("2 in a:", 2 in a)
print("6 in a:", 6 in a)

ab = a.union(b)
print("a union b:", ab)

a_b = a.difference(b)
print("a - b:", a_b)

print("c subset of a:", c.issubset(a))

print("c = d:", c == d)
print("d = c:", d == c)

aib = a.intersection(b)
print("a intersect b:", aib)

a.add(7)
print("add 7 to a:", a)
a.add(2)
print("add 2 to a again:", a)

empty = set()
print("empty:", empty)
print("Is empty set empty?", empty == set())
print("Size of empty set:", len(empty))
print("Is disjoint?", not bool(a.intersection(b)))
print("Unmodifiable set:", collections.abc.MappingProxyType(a))