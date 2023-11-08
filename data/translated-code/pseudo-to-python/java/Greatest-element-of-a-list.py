def max(values):
    max_val = values[0]
    for value in values:
        if max_val < value:
            max_val = value
    return max_val