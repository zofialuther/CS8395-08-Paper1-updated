from itertools import islice

def tails(iterable):
    it = iter(iterable)
    result = [iterable]
    current_tail = list(iterable)
    for _ in iterable:
        next_item = next(it, None)
        if next_item is not None:
            current_tail.pop(0)
            result.append(current_tail)
            current_tail = current_tail[1:] + [next_item]
    return result

def strip_prefix(prefix, iterable):
    if iterable[:len(prefix)] == prefix:
        return iterable[len(prefix):]
    else:
        return None

def count(sub, lst):
    return len([x for x in map(lambda x: strip_prefix(sub, x), tails(lst)) if x is not None])

# Example usage:
print(count([1, 2], [1, 2, 3, 1, 2, 3, 4])) # Output: 2