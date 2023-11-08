```python
class Range:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class RangeSorter:
    def compare(self, range1, range2):
        return range1.left - range2.left

class RangeConsolidation:
    @staticmethod
    def consolidate(ranges):
        ranges.sort(key=lambda x: x.left)
        result = []
        for r in ranges:
            if not result or r.left > result[-1].right:
                result.append(r)
            else:
                result[-1].right = max(result[-1].right, r.right)
        return result

if __name__ == "__main__":
    range1 = Range(1, 3)
    range2 = Range(2, 4)
    range3 = Range(5, 7)
    range4 = Range(6, 8)
    range5 = Range(10, 12)

    input_ranges = [range1, range2, range3, range4, range5]
    print("Original Ranges:")
    for r in input_ranges:
        print(f"({r.left}, {r.right})", end=" ")
    print("\nConsolidated Ranges:")
    consolidated_ranges = RangeConsolidation.consolidate(input_ranges)
    for r in consolidated_ranges:
        print(f"({r.left}, {r.right})", end=" ")
```