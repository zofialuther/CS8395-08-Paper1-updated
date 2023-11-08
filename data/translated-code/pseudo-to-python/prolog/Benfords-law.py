def fib(C, P_S, N):  
    if N == P_S[0] + P_S[1]:
        return True
    else: 
        return False

def fib(C, P_S, Cv, V): 
    if succ(C, Cn) and N == P_S[0] + P_S[1]:
        Cv = Cn
        V = N
        return True
    else:
        return False

def fib_0_0():
    return True

def fib_1_1():
    return True

def fib(C, N): 
    fib(2, [0,1], C, N)
    
def benford(D, Val): 
    Val = log10(1+1/D)

def firstchar(V): 
    if fib(C,N) and N != 0 and atom_chars(N, [Ch|_]) and number_chars(V, [Ch]):
        if C > 999:
            return True
        else:
            return False

def incNth(1, [Dh|Dt], [Ch|Dt]): 
    Dh = Ch

def incNth(H, [Dh|Dt], [Dh|Ct]): 
    if succ(Hn, H):
        incNth(Hn, Dt, Ct)

def freq([], D, D): 
    return True

def freq([H|T], D, C): 
    incNth(H, D, L)
    freq(T, L, C)

def freq([H|T], Freq): 
    Len = len([H|T])
    Min = min([H|T])
    Max = max([H|T])
    between(Min, Max, In)
    freq([H|T], In, F)
    member(V, F)
    N = V/Len
    Freq = N

def writeHdr():
    print('Benford - Measured')

def writeData(Benford, Freq): 
    print(Benford*100 - Freq*100)

def go(): 
    between(1,9,N)
    benford(N,B)
    firstchar(C)
    freq(Fc, Freq)
    writeHdr()
    maplist(writeData, Benford, Freq)