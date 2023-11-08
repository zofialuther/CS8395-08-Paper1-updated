def spell(N, S):
    if N < 0:
        NegN = -N
        spell(NegN, S0)
        S = "negative " + S0
    elif N == 0:
        S = "zero"
    elif 1 <= N <= 19:
        ones(N, S)
    elif N < 100:
        Tens = N // 10
        Ones = N % 10
        tens(Tens, StrTens)
        ones_part(Ones, StrOnes)
        S = StrTens + StrOnes
    elif N < 1000:
        Hundreds = N // 100
        Tens = N % 100
        ones(Hundreds, H)
        StrHundreds = H + " hundred"
        tens_part(Tens, StrTens)
        S = StrHundreds + StrTens
    else:
        spellgroup(N, G)
        group(G, StrG)
        M = 10**(3 * G)
        Group = N // M
        Rest = N % M
        spell(Group, S1)
        spell_remaining(Rest, S2)
        S = S1 + " " + StrG + S2

def ones_part(N, S):
    if N == 0:
        S = ""
    else:
        ones(N, StrN)
        S = "-" + StrN

def tens_part(N, S):
    if N == 0:
        S = ""
    else:
        spell(N, Tens)
        S = " and " + Tens

def spell_remaining(N, S):
    if N == 0:
        S = ""
    else:
        spell(N, Rest)
        S = ", " + Rest