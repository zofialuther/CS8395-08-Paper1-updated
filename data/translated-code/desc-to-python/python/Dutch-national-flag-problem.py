def dutch_flag_sort2(items, order=None):
    filtered_items = [item for item in items if item == order]
    flattened_list = list(itertools.chain(*filtered_items))
    return flattened_list