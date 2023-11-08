s1, s2 = {1, 2, 3, 4}, {3, 4, 5, 6}
print(s1 | s2)  # Union
print(s1 & s2)  # Intersection
print(s1 - s2)  # Difference
print(s1 < s1)  # True subset
print({3, 1} < s1)  # True subset
print(s1 <= s1)  # Subset
print({3, 1} <= s1)  # Subset
print({3, 2, 4, 1} == s1)  # Equality
print(s1 == s2)  # Equality
print(2 in s1)  # Membership
print(10 not in s1)  # Non-membership
print({1, 2, 3, 4, 5} > s1)  # True superset
print({1, 2, 3, 4} > s1)  # True superset
print({1, 2, 3, 4} >= s1)  # Superset
print(s1 ^ s2)  # Symmetric difference
print(len(s1))  # Cardinality
s1.add(99)  # Mutability
print(s1)
s1.discard(99)  # Mutability
print(s1)
s1 |= s2  # Mutability
print(s1)
s1 -= s2  # Mutability
print(s1)
s1 ^= s2  # Mutability
print(s1)