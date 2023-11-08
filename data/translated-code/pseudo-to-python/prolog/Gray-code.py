from itertools import accumulate

def to_gray(N):
    N0 = N >> 1
    G = N ^ N0
    return G

def from_gray(G):
    if G > 0:
        S = G >> 1
        N0 = from_gray(S)
        N = G ^ N0
    else:
        N = G
    return N

def make_num(In):
    Out = int(In)
    return Out

def write_record(Number, Gray, Decoded):
    print("Number: {}, Number in binary: {:05b}, Gray: {}, Decoded: {}, Decoded in specific format: {:02X}".format(Number, Number, Gray, Decoded, Decoded))

def go():
    Numbers = list(range(32))
    Grays = list(map(to_gray, Numbers))
    Decodeds = list(map(from_gray, Grays))
    
    print("Number, Number in binary, Gray, Decoded, Decoded in specific format")
    print("---------------------------------------------------------------")
    list(map(write_record, Numbers, Grays, Decodeds))

def go_err():
    try:
        go()
    except:
        exit(1)