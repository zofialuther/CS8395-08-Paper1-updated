from functools import reduce

def ethMult(n):
    def doubled(x):
        return x + x
    
    def halved(h):
        qr = divmod(h, 2)
        if 0 < h:
            print('halve:', str(qr).rjust(8, ' '))
        return qr if 0 < h else None
    
    def addedWhereOdd(a, remx):
        odd, x = remx
        if odd:
            print(
                str(a).rjust(2, ' '), '+',
                str(x).rjust(3, ' '), '->',
                str(a + x).rjust(3, ' ')
            )
            return a + x
        else:
            print(str(x).rjust(8, ' '))
            return a
    
    def ethMultInner(m):
        return reduce(
            addedWhereOdd,
            zip(
                unfoldr(halved)(n),
                iterate(doubled)(m)
            ),
            0
        )
    
    return ethMultInner

if __name__ == '__main__':
    print(
        '\nProduct:    ' + str(
            ethMult(17)(34)
        ),
        '\n_______________\n'
    )
    print(
        '\nProduct:    ' + str(
            ethMult(34)(17)
        )
    )