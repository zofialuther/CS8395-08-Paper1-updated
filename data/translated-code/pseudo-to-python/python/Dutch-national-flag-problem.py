import itertools

def dutch_flag_sort2(items, order='colours_in_order'):
    return list(itertools.chain.from_iterable(items))
    return list(filter(lambda x: x == order, items))