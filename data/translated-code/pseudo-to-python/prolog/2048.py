```python
def play_2048():
    welcome_msg()
    Grid = [' ']*16
    play(Grid, 'yes')

def welcome_msg():
    print('''
    Welcome to the Prolog version of 2048

    To play using w,s,a,d keys for movement, q to quit
    ''')

def contrats_msg():
    print('Congratulations, you reached 2048!\n')

def loser_msg():
    print('Uh Oh, you could not quite make it to 2048...\n')

def quit_msg():
    print('Bye then!\n')

def player_not_won_yet(Grid):
    return all(x != 2048 for x in Grid)

def player_wins(Grid):
    return 2048 in Grid

def player_loses(G):
    return move('up', G, G) == G and move('down', G, G) == G and move('left', G, G) == G and move('right', G, G) == G

def play(Grid, CreateNewNum):
    if player_wins(Grid):
        draw_grid(Grid)
        contrats_msg()
    elif player_not_won_yet(Grid):
        spaces = [i for i in Grid if i == ' ']
        n_spaces = len(spaces)
        play(Grid, CreateNewNum, n_spaces)

def play(Grid, CreateNewNum, n_spaces):
    if n_spaces == 0:
        play(Grid)
    else:
        play(GridWithRandom)

def play(Grid):
    if player_loses(Grid):
        draw_grid(Grid)
        loser_msg()
    elif not player_loses(Grid):
        draw_grid(Grid)
        move = next_move_by_player()
        player_made_move(Grid, move)

def next_move_by_player():
    while True:
        char = input('Enter your move (w, s, a, d) or q to quit: ')
        return key_move(ord(char))

def key_move(char):
    if char == 119:
        return 'up'
    elif char == 115:
        return 'down'
    elif char == 97:
        return 'left'
    elif char == 100:
        return 'right'
    elif char == 113:
        quit_msg()
        exit()

def draw_grid(Grid):
    print('+-------------------+')
    print(f'| {Grid[0]} | {Grid[1]} | {Grid[2]} | {Grid[3]} |')
    print(f'| {Grid[4]} | {Grid[5]} | {Grid[6]} | {Grid[7]} |')
    print(f'| {Grid[8]} | {Grid[9]} | {Grid[10]} | {Grid[11]} |')
    print(f'| {Grid[12]} | {Grid[13]} | {Grid[14]} | {Grid[15]} |')
    print('+-------------------+\n')

def move(Direction, UnMoved, Moved):
    # Implement map_move, combine_row, partition, append, and other helper functions here
    pass
```