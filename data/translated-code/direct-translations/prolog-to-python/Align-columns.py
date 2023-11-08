```python
def aligner(L):
    # parse the lines and the words
    # compute the length of the longest word
    # LP is the list of lines,
    # each line is a list of words
    parse(L, 0, N, LP, [])

    # we need to add 1 to aligned
    N1 = N + 1
    # words will be left aligned
    AL = '~~w~~t~~~w|'.format(N1)
    # words will be centered
    AC = '~~t~~w~~t~~~w|'.format(N1)
    # words will be right aligned
    AR = '~~t~~w~~~w|'.format(N1)

    print('Left justified :')
    list(map(lambda line: affiche(AL, line), LP))
    print('Centered justified :')
    list(map(lambda line: affiche(AC, line), LP))
    print('Right justified :')
    list(map(lambda line: affiche(AR, line), LP))

def affiche(F, L):
    list(map(lambda word: my_format(F, word), L))
    print()

def my_format(F, W):
    if W == 13:
        print()
    else:
        AW = str(W)
        AF = F.format(AW)
        print(AF)

def parse(T, N, Max, LP=[]):
    if not T:
        return Max
    else:
        N1, T1, L = parse_line(T, 0, N, [], [])
        if N1 > N:
            N2 = N1
        else:
            N2 = N
        LP.append(L)
        return parse(T1, N2, Max, LP)

def parse_line(T, N, NF, TF, L):
    if not T:
        return NF, NF, TF, L
    elif T[0] == '\n':
        return NF, NF, T[1:], L
    else:
        N1, T1, W = parse_word(T, 0, N, [], [])
        if N1 > N:
            N2 = N1
        else:
            N2 = N
        L.append(W)
        return parse_line(T1, N2, NF, TF, L)

# 36 is the code of '$'
def parse_word(T, N, NF, TF, W=[]):
    if not T:
        return N, N, TF, W
    elif T[0] == '$':
        return N, N, T[1:], W
    else:
        N1 = N + 1
        W.append(T[0])
        return parse_word(T[1:], N1, NF, TF, W)
```