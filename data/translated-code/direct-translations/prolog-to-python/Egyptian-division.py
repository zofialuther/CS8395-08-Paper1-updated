def egyptian_divide(Dividend, Divisor):
    Powers = [1]
    Multiples = [Divisor]
    powers2_multiples(Dividend, Powers, Powers, Multiples, Multiples)
    Quotient, Remainder = 0, 0
    accumulate(Dividend, Powers, Multiples, 0, Quotient, 0, Remainder)
    Remainder = Dividend - Remainder
    return Quotient, Remainder

def powers2_multiples(Dividend, Powers, Powers, Multiples, Multiples):
    M = Multiples[0]
    if 2 * M > Dividend:
        return
    else:
        Power2 = 2 * Powers[0]
        Multiple2 = 2 * M
        powers2_multiples(Dividend, [Power2] + Powers, Powers, [Multiple2] + Multiples, Multiples)

def accumulate(Dividend, Powers, Multiples, Ans, Answer, Acc):
    if len(Powers) == 0 or len(Multiples) == 0:
        return Ans, Acc
    P = Powers[0]
    M = Multiples[0]
    if Acc + M <= Dividend:
        Acc = Acc + M
        Ans = Ans + P
        return accumulate(Dividend, Powers[1:], Multiples[1:], Ans, Answer, Acc)
    else:
        return accumulate(Dividend, Powers[1:], Multiples[1:], Ans, Answer, Acc)

def test_egyptian_divide(Dividend, Divisor):
    Quotient, Remainder = egyptian_divide(Dividend, Divisor)
    print(f'{Dividend} / {Divisor} = {Quotient}, remainder = {Remainder}')

def main():
    test_egyptian_divide(580, 34)

main()