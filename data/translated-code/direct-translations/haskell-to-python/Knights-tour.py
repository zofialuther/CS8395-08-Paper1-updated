```python
from functools import reduce
from operator import add
from itertools import permutations

# Knight's Tour
def knight_tour(moves):
    if not possibilities:
        return moves[::-1]
    else:
        return knight_tour([new_square] + moves)
    new_square = min(possibilities, key=lambda x: len(find_moves(x)))
    possibilities = find_moves(moves[0])

def find_moves(square):
    return list(set(knight_options(square)) - set(moves))

def knight_options(square):
    x, y = square
    return list(filter(on_board, map(lambda move: (move[0] + x, move[1] + y), knight_moves)))

def on_board(n):
    return 0 < n < 9

def both(f, xy):
    return (f(xy[0]), f(xy[1]))

# Test
start_point = (5, 5)

def algebraic(square):
    return chr(square[0] + 96) + chr(square[1] + 48)

def main():
    tour = list(map(algebraic, knight_tour([start_point])))
    while tour:
        print(" -> ".join(tour[:8]))
        tour = tour[8:]

main()
```