from random import randint

level = 1

def setup():
    global level
    level = 1

def step():
    global level
    N = randint(0, 3)
    if N > 0:
        level += 1
        print(f'Climbed up to {level}')
    else:
        level -= 1
        print(f'Fell down to {level}')
    if N == 0:
        return False
    return True
setup()
step()