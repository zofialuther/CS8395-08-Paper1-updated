```python
class Disjoint:
    def sortDisjoint(self, lst, indices):
        sorted_elements = [lst[i] for i in indices]
        sorted_elements.sort()
        for i, index in enumerate(indices):
            lst[index] = sorted_elements[i]

if __name__ == "__main__":
    disjoint = Disjoint()
    elements = [5, 2, 8, 3, 1, 9]
    indices = [1, 3, 5]
    disjoint.sortDisjoint(elements, indices)
    print(elements)
```