def substring_task(Str, N, M, Char, SubStr):
    Span = Str[N:M]
    ToEnd = Str[N:]
    MinusLast = Str[:-1]
    FromCharToMth = Str[Str.index(Char):M]
    FromSubToM = Str[Str.index(SubStr):M]
    print('from n to m:', Span)
    print('from n to end:', ToEnd)
    print('string minus last char:', MinusLast)
    print('from known char to m:', FromCharToMth)
    print('from known substring to m:', FromSubToM)

def string_from_substring_to_m(String, Sub, M):
    Before = String.split(Sub)[0]
    FromSubToM = String[Before:M]
    return FromSubToM