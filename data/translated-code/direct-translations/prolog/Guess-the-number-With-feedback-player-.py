```python
def pick_number(Min, Max):
    print(f'Pick a number between {Min} and {Max}, and I will guess it...\nReady? (Enter anything when ready):')
    input()

def guess_number(Min, Max):
    Guess = (Min + Max) // 2
    print(f'I guess {Guess}...\nAm I correct (c), too low (l), or too high (h)? ')
    while True:
        Score = input()
        if Score == 'l':
            NewMin = Guess + 1
            guess_number(NewMin, Max)
        elif Score == 'h':
            NewMax = Guess - 1
            guess_number(Min, NewMax)
        elif Score == 'c':
            print('I am correct!')
            break
        else:
            print('Invalid input')
            continue

def play():
    Min = 1
    Max = 10
    pick_number(Min, Max)
    guess_number(Min, Max)

play()
```