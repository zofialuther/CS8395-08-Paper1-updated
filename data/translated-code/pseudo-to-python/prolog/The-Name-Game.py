def map_name1(C, Cs, Fc, NChars):
    if C == Cs:
        return NChars
    elif C in ['a', 'e', 'i', 'o', 'u']:
        NChars.append(Fc)
        NChars.append(C)
        NChars.append(Cs)
    elif C not in ['a', 'e', 'i', 'o', 'u'] and C != Fc:
        NChars.append(Fc)
        NChars.append(Cs)

def map_name(C, Cs, Fc, Name):
    NChars = map_name1(C, Cs, Fc, [])
    Name = ''.join(NChars)

def song(Name):
    LName = Name.lower()
    First = LName[0]
    Chars = LName[1:]
    BName = map_name(First, Chars, 'b', [])
    FName = map_name(First, Chars, 'f', [])
    MName = map_name(First, Chars, 'm', [])
    print(Name, ", ", Name, ", bo-", BName, '\n')
    print("Banana-fana fo-", FName, '\n')
    print("Fee-fi-mo-", MName, '\n')
    print(Name, "!\n\n")

def test():
    for name in ["Gary", "Earl", "Billy", "Felix", "Mary"]:
        song(name)