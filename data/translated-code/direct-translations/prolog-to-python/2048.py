```python
import random

def play_2048():
    welcome_msg()
    grid = [' ']*16
    play(grid, 'yes')

def welcome_msg():
    print("\nWelcome to the Prolog version of 2048\n")
    print("To play using w,s,a,d keys for movement, q to quit\n")

def contrats_msg():
    print("Congratulations, you reached 2048!\n")

def loser_msg():
    print("Uh Oh, you could not quite make it to 2048...\n")

def quit_msg():
    print("Bye then!\n")

def player_not_won_yet(grid):
    return all(x != 2048 for x in grid)

def player_wins(grid):
    return 2048 in grid

def player_loses(grid):
    return move('up', grid[:], grid) == grid and move('down', grid[:], grid) == grid and move('left', grid[:], grid) == grid and move('right', grid[:], grid) == grid

def play(grid, create_new_num):
    if player_wins(grid):
        draw_grid(grid)
        contrats_msg()
    elif player_not_won_yet(grid):
        spaces = [x for x in grid if x == ' ']
        n_spaces = len(spaces)
        play(grid, create_new_num, n_spaces)

def next_move_by_player():
    while True:
        char = input("Enter your move (w/a/s/d to move, q to quit): ")
        if char == 'w':
            return 'up'
        elif char == 's':
            return 'down'
        elif char == 'a':
            return 'left'
        elif char == 'd':
            return 'right'
        elif char == 'q':
            return 'quit'

def draw_grid(grid):
    print('+-------------------+')
    print_row(grid[0:4])
    print_row(grid[4:8])
    print_row(grid[8:12])
    print_row(grid[12:16])
    print('¦\n+-------------------+\n\n\n')

def print_row(row):
    print('¦', end='')
    for x in row:
        if x == ' ':
            print('    ', end='')
        else:
            print('  {:4d}'.format(x), end='')
    print('¦')

def random_space(n, grid):
    if n == 0:
        return grid
    elif n == 1:
        v = 4 if random.randint(1, 10) == 1 else 2
        i = grid.index(' ')
        grid[i] = v
        return grid
    else:
        v = 4 if random.randint(1, 10) == 1 else 2
        p = random.randint(0, n-1)
        i = grid.index(' ')
        grid[i] = v
        return random_space(p, grid)

def replace_space(p, v, grid):
    if p == 0:
        i = grid.index(' ')
        grid[i] = v
        return grid
    else:
        i = grid.index(' ')
        return replace_space(p-1, v, grid[:i] + [grid[i]] + grid[i+1:])

def move(direction, unmoved, moved):
    unmoved_mapped = map_move(direction, unmoved)
    moved_mapped = [combine_row(row) for row in unmoved_mapped]
    return map_move(direction, moved, moved_mapped)

def map_move(direction, grid):
    if direction == 'up':
        return [[grid[12+i], grid[8+i], grid[4+i], grid[i]] for i in range(4)]
    elif direction == 'down':
        return [[grid[i], grid[i+4], grid[i+8], grid[i+12]] for i in range(4)]
    elif direction == 'left':
        return [grid[i*4:i*4+4] for i in range(4)]
    elif direction == 'right':
        return [grid[i*4:i*4+4][::-1] for i in range(4)]

def combine_row(row):
    blank, set_ = [], []
    for x in row:
        if x == ' ':
            blank.append(x)
        else:
            set_.append(x)
    ready_to_move = blank + set_
    return combine(ready_to_move)

def combine(row):
    if len(row) == 4:
        a, b, c, d = row
        if a != b and b != c and c != d:
            return row
        elif a == b and b != c and c != d:
            return [' ', ' ', a*2, d]
        elif a != b and b == c and c != d:
            return [' ', a, b*2, d]
        elif a != b and b != c and c == d:
            return [a, b, ' ', c*2]
        elif a != b and b == c and c == d:
            return [' ', a, b*2, c*2]
        elif a == b and b != c and c == d:
            return [' ', ' ', a*2, c*2]

def main():
    play_2048()

if __name__ == "__main__":
    main()
```