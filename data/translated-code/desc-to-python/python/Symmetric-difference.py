setA = {"Alice", "Bob", "Charlie", "David"}
setB = {"David", "Edward", "Alice", "Frank"}

symmetric_difference = setA.symmetric_difference(setB)
unique_elements = setA.union(setB) - setA.intersection(setB)
union_set = setA.union(setB)
intersection_set = setA.intersection(setB)

print("Symmetric Difference:", symmetric_difference)
print("Unique Elements:", unique_elements)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)