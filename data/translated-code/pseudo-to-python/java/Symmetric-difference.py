```python
class SymmetricDifference:
    def main(self):
        setA = {1, 2, 3, 4, 5}
        setB = {4, 5, 6, 7, 8}
        print("Initial data set for setA:", setA)
        print("Initial data set for setB:", setB)
        
        notInSetA = setB.difference(setA)
        notInSetB = setA.difference(setB)
        symmetricDifference = notInSetA.union(notInSetB)
        union = setA.union(setB)
        intersection = setA.intersection(setB)
        symmetricDifference2 = union.difference(intersection)
        
        print("Elements not in setA but in setB:", notInSetA)
        print("Elements not in setB but in setA:", notInSetB)
        print("Symmetric Difference:", symmetricDifference)
        print("Symmetric Difference using union and intersection:", symmetricDifference2)

SymmetricDifference().main()
```