from ordered_set import OrderedSet

A = OrderedSet([1,2,3,4])
B = OrderedSet([2,4,6,8])

print(2 in A)

Union = A.union(B)

Intersection = A.intersection(B)

Diff = A.difference(B)

print(A.issubset(B))
print(OrderedSet([2,4]).issubset(B))

print(A == B)
print(A == OrderedSet([1,2,3,4]))

def ord_propsubset(A, B):
    return A.issubset(B) and A != B

NewA = A.copy()
NewA.add(19)

NewerA = NewA.copy()
NewerA.discard(3)