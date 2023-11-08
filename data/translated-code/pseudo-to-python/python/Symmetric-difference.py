setA = {"John", "Bob", "Mary", "Serena"}
setB = {"Jim", "Mary", "John", "Bob"}

symmetric_difference = setA.symmetric_difference(setB)
elements_in_A_not_in_B = setA.difference(setB)
elements_in_B_not_in_A = setB.difference(setA)
union = setA.union(setB)
intersection = setA.intersection(setB)

print(symmetric_difference) 
print(elements_in_A_not_in_B) 
print(elements_in_B_not_in_A) 
print(union) 
print(intersection)