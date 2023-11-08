```python
def knightTour(n, path, u, limit):
    if n == limit:
        return True
    for v in knightOptions(u):
        if v not in path:
            path.append(v)
            if knightTour(n+1, path, v, limit):
                return True
            path.pop()
    return False

def knightOptions(u):
    # calculate and return all possible legal moves for knight from square u
    pass

def main(starting_point):
    # convert algebraic notation to internal representation
    # call knightTour and print out the sequence of moves in algebraic notation
    pass
```