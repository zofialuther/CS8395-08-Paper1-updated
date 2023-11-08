def dutch_flag_sort2(items, order=colours_in_order):
    return list(chain.from_iterable(filter(lambda c: c==colour, items) for colour in order))