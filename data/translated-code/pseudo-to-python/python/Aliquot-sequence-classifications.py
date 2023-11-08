def proper_divs(n):
    # code for proper_divs function

def pdsum(n):
    return sum(proper_divs(n))

def aliquot(n, maxlen=16, maxterm=2**47):
    if n == 0:
        return 'terminating', [0]
    s, slen, new = [n], 1, n
    while slen <= maxlen and new < maxterm:
        new = pdsum(s[-1])
        if new in s:
            if s[0] == new:
                if slen == 1:
                    return 'perfect', s
                elif slen == 2:
                    return 'amicable', s
                else:
                    return 'sociable of length ' + str(slen), s
            elif s[-1] == new:
                return 'aspiring', s
            else:
                return 'cyclic back to ' + str(new), s
        elif new == 0:
            return 'terminating', s + [0]
        else:
            s.append(new)
            slen = slen + 1
    return 'non-terminating', s

if __name__ == '__main__':
    for n in range(1, 11):
        print(str(aliquot(n)))
    print()
    for n in [11, 12, 28, 496, 220, 1184,  12496, 1264460, 790, 909, 562, 1064, 1488, 15355717786080]:
        print(str(aliquot(n)))