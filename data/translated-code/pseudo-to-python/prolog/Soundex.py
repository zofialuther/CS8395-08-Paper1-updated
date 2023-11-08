def creplace(Ch, result):
    if Ch in "bfpv":
        return result.replace(Ch, '1')
    elif Ch in "cgjkqsxz":
        return result.replace(Ch, '2')
    elif Ch in "dt":
        return result.replace(Ch, '3')
    elif Ch == 'l':
        return result.replace(Ch, '4')
    elif Ch in "mn":
        return result.replace(Ch, '5')
    elif Ch == 'r':
        return result.replace(Ch, '6')

def strip(Set, T, Tr):
    if T:
        H = T[0]
        T = T[1:]
        if H in Set:
            return strip(Set, T, Tr)
        else:
            Tr.append(H)
            return strip(Set, T, Tr)
    else:
        return Tr

def consonants(T, Tr):
    if T:
        H = T[0]
        T = T[1:]
        result = creplace(H, H)
        Tr.append(result)
        return consonants(T, Tr)
    else:
        return Tr

def adjacent(T, Tr):
    if len(T) > 1:
        Ch = T[0]
        if ord('0') <= ord(Ch) <= ord('9'):
            return adjacent(T[1:], Tr)
        else:
            Tr.append(Ch)
            return adjacent(T[1:], Tr)
    else:
        return Tr

def chk_digit(T, Tr):
    if len(T) > 1:
        H = T[0]
        D = T[1]
        if ord('0') <= ord(D) <= ord('9'):
            return chk_digit(T[2:], Tr)
        else:
            Tr.append(H)
            return chk_digit(T[1:], Tr)
    else:
        return Tr

def do_soundex(T, Res):
    Ts = strip("hw", T, [])
    Tc = consonants(Ts, [])
    Ta = adjacent(Tc, [])
    Tv = strip("aeiouy", Ta, [])
    Td = chk_digit([T[0]] + Tv, [])
    Tr = Td + "0000"
    Tf = ''.join(Tr)
    Res = Tf[:4]
    return Res

def soundex(Text, Res):
    Lower = Text.lower()
    T = list(Lower)
    return do_soundex(T, Res)

def test():
    if soundex('Robert', 'r163') != 'r163':
        print('Robert failed')
    if soundex('Rupert', 'r163') != 'r163':
        print('Rupert failed')
    if soundex('Rubin', 'r150') != 'r150':
        print('Rubin failed')
    if soundex('Ashcroft', 'a261') != 'a261':
        print('Ashcroft failed')
    if soundex('Ashcraft', 'a261') != 'a261':
        print('Ashcraft failed')
    if soundex('Tymczak', 't522') != 't522':
        print('Tymczak failed')
    if soundex('Pfister', 'p236') != 'p236':
        print('Pfister failed')

test()