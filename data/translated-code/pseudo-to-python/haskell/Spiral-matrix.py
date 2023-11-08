def spiral(h, w, s):
    if h == 0:
        return [[]]
    else:
        return [list(range(s, s+w))] + rot90(spiral(w, h-1, s+w))

def rot90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def main():
    rows = spiral(10, 9, 1)
    for row in rows:
        for num in row:
            print(f"{num:4d}", end="")
        print("")