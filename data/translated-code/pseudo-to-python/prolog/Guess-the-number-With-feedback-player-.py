def pick_number(Min, Max):
    print('Pick a number between ' + str(Min) + ' and ' + str(Max) + ', and I will guess it...')
    print('Ready? (Enter anything when ready):')
    input()

def guess_number(Min, Max):
    Guess = (Min + Max) // 2
    print('I guess ' + str(Guess) + '...')
    print('Am I correct (c), too low (l), or too high (h)? ')
    Score = input()
    while True:
        if Score == 'l':
            NewMin = Guess + 1
            guess_number(NewMin, Max)
        elif Score == 'h':
            NewMax = Guess - 1
            guess_number(Min, NewMax)
        elif Score == 'c':
            print('I am correct!')
        else:
            print('Invalid input')
            return False

def play():
    Min = 1
    Max = 100
    pick_number(Min, Max)
    guess_number(Min, Max)