def consolidate_ranges(Ranges):
    def normalize(ranges):
        normalized = []
        for r in ranges:
            if r[0] > r[1]:
                normalized.append((r[1], r[0]))
            else:
                normalized.append((r[0], r[1]))
        return normalized

    def merge(normalized):
        sorted_ranges = sorted(normalized)
        merged = [sorted_ranges[0]]
        for r in sorted_ranges[1:]:
            if r[0] <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
            else:
                merged.append(r)
        return merged

    def write_range(r):
        print(f'[{r[0]}, {r[1]}]', end='')

    def write_ranges(ranges):
        for i, r in enumerate(ranges):
            write_range(r)
            if i < len(ranges) - 1:
                print(', ', end='')
        print()

    for ranges in Ranges:
        normalized = normalize(ranges)
        consolidated = merge(normalized)
        write_ranges(ranges)
        print(' -> ', end='')
        write_ranges(consolidated)

test_cases = [
    [(1.1, 2.2)],
    [(6.1, 7.2), (7.2, 8.3)],
    [(4, 3), (2, 1)],
    [(4, 3), (2, 1), (-1, -2), (3.9, 10)],
    [(1, 3), (-6, -1), (-4, -5), (8, 2), (-6, -6)]
]

consolidate_ranges(test_cases)