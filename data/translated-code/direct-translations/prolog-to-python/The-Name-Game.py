def map_name1(C, Cs, C, Cs):
    return True

def map_name1(C, Cs, Fc, [Fc,C|Cs]):
    if C in ['a','e','i','o','u']:
        return True
    else:
        return False

def map_name1(C, Cs, Fc, [Fc|Cs]):
    if C not in ['a','e','i','o','u'] and C != Fc:
        return True
    else:
        return False

def map_name(C, Cs, Fc, Name):
    NChars = []
    if map_name1(C, Cs, Fc, NChars):
        Name = ''.join(NChars)
        return Name

def song(Name):
    LName = Name.lower()
    First = LName[0]
    Chars = list(LName[1:])

    BName = map_name(First, Chars, 'b', BName)
    FName = map_name(First, Chars, 'f', FName)
    MName = map_name(First, Chars, 'm', MName)

    print(Name + ", " + Name + ", bo-" + BName)
    print("Banana-fana fo-" + FName)
    print("Fee-fi-mo-" + MName)
    print(Name + "!\n")

def test():
    names = ["Gary", "Earl", "Billy", "Felix", "Mary"]
    for name in names:
        song(name)