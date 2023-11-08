def between(start, end):
    for val in range(start, end+1):
        yield val

for val in between(1, 10):
    print(val, end=', ')
print()