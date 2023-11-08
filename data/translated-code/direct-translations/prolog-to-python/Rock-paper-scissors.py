```python
import random

def play():
    Prev = [P for P,_ in beats]
    play_round(Prev)

def play_round(Prev):
    print('your choice? ')
    P = input()
    C = random.choice(Prev)
    print('The computer chose', C)
    result(C, P, Prev)

def result(C, P, Prev):
    if (C, P) in beats:
        print('Computer wins.')
        Next = [C] + Prev
    elif (P, C) in beats:
        print('You win!')
        Next = [P] + Prev
    else:
        print('It is a draw')
        Next = [C] + Prev
    play_round(Next)

beats = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]

play()
```