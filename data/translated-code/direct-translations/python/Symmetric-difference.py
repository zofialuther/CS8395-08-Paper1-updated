setA = {"John", "Bob", "Mary", "Serena"}
setB = {"Jim", "Mary", "John", "Bob"}
print(setA.symmetric_difference(setB)) # symmetric difference of A and B
print(setA.difference(setB)) # elements in A that are not in B
print(setB.difference(setA)) # elements in B that are not in A
print(setA.union(setB)) # elements in A or B (union)
print(setA.intersection(setB)) # elements in both A and B (intersection)