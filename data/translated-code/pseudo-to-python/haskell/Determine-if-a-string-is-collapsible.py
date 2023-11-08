from itertools import groupby

def is_collapsible(s):
    return any(len(list(g)) > 1 for k, g in groupby(s))

def collapsed(s):
    return ''.join(k for k, g in groupby(s))