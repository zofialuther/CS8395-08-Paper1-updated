```python
import curses
from random import randrange, choice
from collections import defaultdict

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]

class GameField(object):
    # remaining class code

def main(stdscr):
    curses.use_default_colors()
    game_field = GameField(win=32)
    state_actions = {}  # Init, Game, Win, Gameover, Exit
    # remaining main code

state = 'Init'
while state != 'Exit':
    state = state_actions[state]()
```