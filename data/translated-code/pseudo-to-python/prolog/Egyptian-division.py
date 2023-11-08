def egyptian_divide(Dividend, Divisor):
    Powers = [1]
    Multiples = [Divisor]
    Powers, Multiples = powers2_multiples(Dividend, Powers, Multiples)
    Quotient, _ = accumulate(Dividend, Powers, Multiples, 0, 0)
    Remainder = Dividend - Quotient * Divisor
    return Quotient, Remainder

def powers2_multiples(Dividend, Powers, Multiples):
    if 2 * Multiples[-1] > Dividend:
        return Powers, Multiples
    else:
        Power2 = 2 * Powers[-1]
        Multiple2 = 2 * Multiples[-1]
        Powers.append(Power2)
        Multiples.append(Multiple2)
        return powers2_multiples(Dividend, Powers, Multiples)

def accumulate(Dividend, Powers, Multiples, Ans, Acc):
    if not Powers or not Multiples or Acc + Multiples[0] > Dividend:
        return Ans, Acc
    else:
        Acc1 = Acc + Multiples[0]
        Ans1 = Ans + Powers[0]
        return accumulate(Dividend, Powers[1:], Multiples[1:], Ans1, Acc1)

def test_egyptian_divide(Dividend, Divisor):
    Quotient, Remainder = egyptian_divide(Dividend, Divisor)
    print(f"{Dividend} / {Divisor} = {Quotient}, remainder = {Remainder}")

test_egyptian_divide(580, 34)