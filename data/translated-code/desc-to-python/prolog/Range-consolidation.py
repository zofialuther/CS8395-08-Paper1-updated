```python
def consolidate_ranges(ranges):
    def normalize_range(range):
        return (min(range), max(range))

    def merge_ranges(range1, range2):
        return (min(range1[0], range2[0]), max(range1[1], range2[1]))

    normalized_ranges = [normalize_range(range) for range in ranges]
    normalized_ranges.sort()
    consolidated_ranges = [normalized_ranges[0]]

    for current_range in normalized_ranges[1:]:
        if current_range[0] <= consolidated_ranges[-1][1]:
            consolidated_ranges[-1] = merge_ranges(consolidated_ranges[-1], current_range)
        else:
            consolidated_ranges.append(current_range)

    return consolidated_ranges

def write_single_range(range):
    return f"[{range[0]} - {range[1]}]"

def write_ranges(ranges):
    return ", ".join(write_single_range(range) for range in ranges)

def test_cases():
    ranges1 = [(1, 3), (2, 5), (6, 8), (10, 15)]
    ranges2 = [(1, 5), (3, 7), (6, 8), (10, 12)]
    ranges3 = [(1, 3), (2, 6), (8, 10), (15, 18)]

    print("Original List of Ranges:")
    print("Test Case 1:", write_ranges(ranges1))
    print("Test Case 2:", write_ranges(ranges2))
    print("Test Case 3:", write_ranges(ranges3))

    print("\nConsolidated List of Ranges:")
    print("Test Case 1:", write_ranges(consolidate_ranges(ranges1)))
    print("Test Case 2:", write_ranges(consolidate_ranges(ranges2)))
    print("Test Case 3:", write_ranges(consolidate_ranges(ranges3))

if __name__ == "__main__":
    test_cases()
```