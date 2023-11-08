def range_extract(iterable):
    start = None
    end = None
    for num in iterable:
        if start is None:
            start = num
            end = num
        elif num == end + 1:
            end = num
        else:
            yield (start, end) if start != end else (start,)
            start = num
            end = num
    yield (start, end) if start != end else (start,)

def printr(ranges):
    for r in ranges:
        if len(r) == 1:
            print(f"{r[0]}")
        else:
            print(f"{r[0]}->{r[1]}")

example1 = [1, 2, 3, 6, 7, 9, 10, 11, 12]
example2 = [5, 7, 8, 10, 11]

result1 = range_extract(example1)
result2 = range_extract(example2)

printr(result1)
printr(result2)