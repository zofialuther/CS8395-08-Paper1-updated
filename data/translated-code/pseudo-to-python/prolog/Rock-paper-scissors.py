from random import choice

def play():
    prev = [p for p, _ in beats]
    play_round(prev)

def play_round(prev):
    p = input('your choice? ')
    c = choice(prev)
    print(f'The computer chose {c}')
    result(c, p, prev)

def result(c, p, prev):
    if (c, p) in beats:
        print('Computer wins.')
        prev.append(c)
    elif (p, c) in beats:
        print('You win!')
        prev.append(p)
    else:
        print('It is a draw')
        prev.append(choice([c, p]))
    play_round(prev)

beats = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]

play()