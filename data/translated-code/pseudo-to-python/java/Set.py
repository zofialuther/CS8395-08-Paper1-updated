a = set([1, 2, 3, 4, 5])
b = set([2, 3, 4, 5, 6, 8])
c = set([2, 3, 4])
d = set([2, 3, 4])

print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))

print("2 in a: " + str(2 in a))
print("6 in a: " + str(6 in a))

ab = a.union(b)
print("a union b: " + str(ab))

a_b = a.difference(b)
print("a - b: " + str(a_b))

print("c subset of a: " + str(c.issubset(a)))

print("c = d: " + str(c == d))
print("d = c: " + str(d == c))

aib = a.intersection(b)
print("a intersect b: " + str(aib))

print("add 7 to a: " + str(a.add(7)))
print("add 2 to a again: " + str(a.add(2)))

empty = set()
empty.is_empty()
empty.size()
set.isdisjoint(a, b)
set = frozenset(a)