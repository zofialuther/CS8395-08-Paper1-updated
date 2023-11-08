```python
def consolidate_ranges(Ranges, Consolidated):
    Normalized = normalize(Ranges)
    Sorted = sorted(Normalized)
    merge(Sorted, Consolidated)

def normalize(Ranges):
    Normalized = []
    for r in Ranges:
        X = r[0]
        Y = r[1]
        if X > Y:
            Min = Y
            Max = X
        else:
            Min = X
            Max = Y
        Normalized.append((Min, Max))
    return Normalized

def merge(Sorted, Consolidated):
    Merged = []
    for i in range(len(Sorted)):
        if i == 0:
            Merged.append(Sorted[i])
        else:
            Min1, Max1 = Merged[-1]
            Min2, Max2 = Sorted[i]
            if Min2 <= Max1:
                Merged[-1] = (Min1, max(Max1, Max2))
            else:
                Merged.append((Min2, Max2))
    Consolidated.extend(Merged)

def write_range(Range):
    print(f'[{Range[0]}, {Range[1]}]', end="")

def write_ranges(Ranges):
    for i in range(len(Ranges)):
        write_range(Ranges[i])
        if i < len(Ranges) - 1:
            print(", ", end="")
    print("")

def test_case(Ranges):
    Consolidated = []
    consolidate_ranges(Ranges, Consolidated)
    write_ranges(Ranges)
    print(" -> ", end="")
    write_ranges(Consolidated)

def main():
    test_case([(1.1, 2.2)])
    test_case([(6.1, 7.2), (7.2, 8.3)])
    test_case([(4, 3), (2, 1)])
    test_case([(4, 3), (2, 1), (-1, -2), (3.9, 10)])
    test_case([(1, 3), (-6, -1), (-4, -5), (8, 2), (-6, -6)])

main()
```