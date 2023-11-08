def sort(col):
    if col is None or len(col) == 0:
        return []
    else:
        pivot = col[0]
        grouped = {}
        for item in col:
            comparison = pivot.compare_to(item)
            if comparison not in grouped:
                grouped[comparison] = [item]
            else:
                grouped[comparison].append(item)
        return sorted(grouped[1]) + grouped[0] + sorted(grouped[-1])