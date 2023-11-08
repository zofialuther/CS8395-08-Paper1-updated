def dutch_flag(N):
    L = [init() for _ in range(N)]
    while not is_dutch_flag(L):
        print(L)
        test_sorted(L)
        tmp_flag = sort_dutch_flag(L)
        Flag.append(tmp_flag)
        print(Flag)
        test_sorted(Flag)

def sort_dutch_flag([]):
    return [[], [], []]

def sort_dutch_flag([blue | T]):
    [R, W, B] = sort_dutch_flag(T)
    return [R, W, [blue | B]]

def sort_dutch_flag([red | T]):
    [R, W, B] = sort_dutch_flag(T)
    return [[red | R], W, B]

def sort_dutch_flag([white | T]):
    [R, W, B] = sort_dutch_flag(T)
    return [R, [white | W], B]

def init():
    import random
    colors = ['blue', 'red', 'white']
    return random.choice(colors)

def test_sorted(Flag):
    if is_dutch_flag(Flag):
        print('it is a dutch flag')
    else:
        print('it is not a dutch flag')

def is_dutch_flag([red | T]):
    return is_dutch_flag_red(T)

def is_dutch_flag_red([red | T]):
    return is_dutch_flag_red(T) or (T[:1] == 'white' and is_dutch_flag_white(T[1:]))

def is_dutch_flag_white([white | T]):
    return is_dutch_flag_white(T) or (T[:1] == 'blue' and is_dutch_flag_blue(T[1:]))

def is_dutch_flag_blue([blue | T]):
    return is_dutch_flag_blue(T)

def is_dutch_flag_blue([]):
    return True