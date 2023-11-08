import itertools

def to_gray(N):
    N0 = N >> 1
    return N ^ N0

def from_gray(G):
    if G > 0:
        S = G >> 1
        N0 = from_gray(S)
        return G ^ N0
    else:
        return G

def make_num(In):
    Out, _ = atom_to_term(In)
    return isinstance(Out, int)

def write_record(Number, Gray, Decoded):
    print(f"{Number:10d}|{Number:10b}+{Gray:10b}+{Decoded:10b}+{Decoded}")

def go():
    Numbers = [n for n in range(32)]
    Grays = map(to_gray, Numbers)
    Decodeds = map(from_gray, Grays)

    print(f'{"Number":10s} {"Binary":10s} {"Gray":10s} {"Decoded":10s} {"Number":10s}')
    print(f'{"------":10s} {"------":10s} {"----":10s} {"-------":10s} {"------":10s}')

    for record in itertools.zip_longest(Numbers, Grays, Decodeds):
        write_record(*record)
    return 1

go()