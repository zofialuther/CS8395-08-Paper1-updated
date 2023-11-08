```python
import sys
import random
from random import sample
from random import randint
from termcolor import colored
from colorama import init, Fore, Back, Style
from itertools import product
from colorama import init
init()

# Logic

# probability to get a 4
prob4 = 0.1

Position = [[int]]

def combine(l):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        return [l[0]]
    else:
        if l[0] == l[1]:
            return [2 * l[0]] + combine(l[2:])
        else:
            return [l[0]] + combine(l[1:])

def shift(l):
    return (combine([x for x in l if x != 0]) + [0] * len([x for x in l if x == 0]))[:len(l)]

def reflect(l):
    return [row[::-1] for row in l]

def left(pos):
    return list(map(shift, pos))

def right(pos):
    return reflect(left(reflect(pos)))

def transpose(pos):
    return [list(row) for row in zip(*pos)]

def up(pos):
    return transpose(left(transpose(pos)))

def down(pos):
    return transpose(right(transpose(pos)))

def progress(f, pos):
    next_pos = f(pos)
    if pos == next_pos:
        return None
    else:
        return next_pos

def lost(pos):
    for move in [left, right, up, down]:
        if all(progress(move, pos) == None):
            return True
    return False

def win(pos):
    for row in pos:
        if 2048 in row:
            return True
    return False

def go(pos, move):
    if move == None:
        return None
    else:
        return progress(move, pos)

# or with lens:
def indicesOf(l):
    return [i for i in range(len(l))]

def indices2Of(ls):
    indices = []
    for i in indicesOf(ls):
        l = ls[i]
        for j in indicesOf(l):
            indices.append((i, j))
    return indices

def add2or4(pos):
    xy = random.choice([xy for xy in indices2Of(pos) if pos[xy[0]][xy[1]] == 0])
    a = random.choices([2, 4], weights=[1-prob4, prob4], k=1)[0]
    pos[xy[0]][xy[1]] = a
    return pos

# Main loop
def play(pos):
    c = input("Enter move (W/A/S/D) or Q: ").upper()
    if c == "Q":
        sys.exit(0)
    moves = {'A': left, 'D': right, 'W': up, 'S': down}
    if c in moves:
        move = moves[c]
        pos1 = go(pos, move)
        if pos1 == None:
            play(pos)
        else:
            pos2 = add2or4(pos1)
            draw(pos2)
            if win(pos2) and not win(pos):
                print("You win! You may keep going.")
            if lost(pos2):
                print("You lost!")
            else:
                play(pos2)
    else:
        play(pos)

def main():
    pos = [[0 for i in range(4)] for j in range(4)]
    pos = add2or4(pos)
    draw(pos)
    play(pos)

# Rendering
def draw(pos):
    for i in range(4):
        for j in range(4):
            print(colored('{:6}'.format(pos[i][j]), 'white', 'on_red', attrs=['bold']), end='')
        print()

if __name__ == "__main__":
    main()
```