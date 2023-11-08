```python
def spell(N, S):
    if N < 0:
        NegN = -N
        S0 = spell(NegN)
        S = "negative " + S0
    elif N == 0:
        S = "zero"
    elif 1 <= N <= 19:
        ones_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
        S = ones_dict[N]
    elif N < 100:
        Tens, Ones = divmod(N, 10)
        tens_dict = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
        StrTens = tens_dict[Tens]
        StrOnes = ones(N)
        S = StrTens + StrOnes
    elif N < 1000:
        Hundreds, Tens = divmod(N, 100)
        H = ones(Hundreds)
        StrHundreds = H + " hundred"
        StrTens = tens_part(Tens)
        S = StrHundreds + StrTens
    else:
        G = spellgroup(N)
        group_dict = {1: "thousand", 2: "million", 3: "billion", 4: "trillion", 5: "quadrillion", 6: "quintillion", 7: "sextillion", 8: "septillion", 9: "octillion", 10: "nonillion", 11: "decillion"}
        StrG = group_dict[G]
        M = 10**(3*G)
        Group, Rest = divmod(N, M)
        S1 = spell(Group)
        S2 = spell_remaining(Rest)
        S = f"{S1} {StrG} {S2}"
    return S

def ones(N):
    ones_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    return ones_dict[N]

def tens_part(N):
    if N == 0:
        return ""
    else:
        Tens = spell(N)
        return " and " + Tens

def spell_remaining(N):
    if N == 0:
        return ""
    else:
        Rest = spell(N)
        return ", " + Rest

def spellgroup(N):
    return int(math.floor(math.log10(N) / 3))
```