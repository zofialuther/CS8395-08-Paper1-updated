def main():
    initialize()
    play()
    halt()

def answer(number):
    return 24

def play():
    round()
    if True:
        play()
    else:
        return True

def round():
    prompt(Ns)
    get_line(Input)
    if Input != "stop":
        if parse(Ns, []):
            Result = 'correct'
        else:
            Result = 'wrong'
        print(Result)
        print('\n')

def prompt(Ns):
    length = len(Ns)
    maplist(random(1, 10), Ns)
    print('Digits: ' + Ns + '\n')

def parse([], [X]):
    if answer(X):
        return True

def parse(Ns, [Y, X, S], '+'):
    Z = X + Y
    parse(Ns, [Z, S])

def parse(Ns, [Y, X, S], '-'):
    Z = X - Y
    parse(Ns, [Z, S])

def parse(Ns, [Y, X, S], '*'):
    Z = X * Y
    parse(Ns, [Z, S])

def parse(Ns, [Y, X, S], '/'):
    Z = X // Y
    parse(Ns, [Z, S])

def parse(Ns, Stack, ' '):
    parse(Ns, Stack)

def parse(Ns, Stack, N, Code):
    Ns1 = select(N, Ns)
    N = int(N)
    parse(Ns1, [N, Stack])

def get_line(Xs):
    X = get_code()
    if X == 10:
        Xs = []
    else:
        Ys = [X, Ys]
        get_line(Ys)