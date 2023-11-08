```python
def nim(N):
    next_turn(12)

def next_turn(N):
    # Player Turn
    PlayerGuess = int(input('How many dots would you like to take? '))
    if PlayerGuess in [1, 2, 3]:
        N1 = N - PlayerGuess
        print(f'You take {PlayerGuess} dots\n{N1} dots remaining.\n')

        # Computer Turn
        CompGuess = 4 - PlayerGuess
        N2 = N1 - CompGuess
        print(f'Computer takes {CompGuess} dots\n{N2} dots remaining.\n')

        if N2 == 0:
            print('Computer wins!')
        else:
            next_turn(N2)

nim(12)
```