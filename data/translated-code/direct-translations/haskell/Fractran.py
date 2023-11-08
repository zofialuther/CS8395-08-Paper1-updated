from typing import List

def mapMaybe(func, lst):
    return list(filter(None, map(func, lst)))

def elemIndex(elem, lst):
    try:
        return lst.index(elem)
    except ValueError:
        return None