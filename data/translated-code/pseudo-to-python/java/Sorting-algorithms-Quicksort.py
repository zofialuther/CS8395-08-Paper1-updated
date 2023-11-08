def sort(col):
    if col is None or len(col) == 0:
        return []
    else:
        pivot = col[0]
        grouped = {1: [], 0: [], -1: []}
        for item in col:
            if item > pivot:
                grouped[1].append(item)
            elif item < pivot:
                grouped[-1].append(item)
            else:
                grouped[0].append(item)
        
        return sort(grouped[1]) + grouped[0] + sort(grouped[-1])