def reverse_number(Number, Rev):
    reverse_number(Number, 0, Rev)

def reverse_number(N, R, Rev):
    if N == 0:
        Rev = R
        return
    else:
        R1 = R * 10 + N % 10
        N1 = N // 10
        reverse_number(N1, R1, Rev)

def lychrel(N, M, Cache, Seeds, Related, Palindromes):
    if M > N:
        return
    else:
        R = reverse_number(M)
        lychrel_sequence(M, 0, M, R, Cache, Sequence, Result)
        update_cache(Cache, Sequence, Result, Cache1)
        M1 = M + 1
        if Result == 0:
            S = Seeds
            Rel = Related
            P = Palindromes
        else:
            if R == M:
                Palindromes.append(M)
            else:
                Palindromes = Palindromes
            if Result == M:
                Seeds.append(M)
                Related = Rel
            else:
                Seeds = S
                Related.append(M)
        lychrel(N, M1, Cache1, S, Rel, P)

def update_cache(Cache, Seq, Result, Cache2):
    if not Seq:
        Cache2 = Cache
        return
    else:
        S = Seq[0]
        Seq = Seq[1:]
        put_assoc(S, Cache, Result, Cache1)
        update_cache(Cache1, Seq, Result, Cache2)

def lychrel_sequence(N, I, Sum, Rev, Cache, Sequence, Result):
    if I == 500:
        Result = N
        return
    else:
        I1 = I + 1
        Sum1 = Sum + Rev
        Rev1 = reverse_number(Sum1)
        if (Rev1 == Sum1 and Result == 0) or get_assoc(Sum1, Cache, Result):
            Sequence = []
        else:
            lychrel_sequence(N, I1, Sum1, Rev1, Cache, Sequence, Result)

def lychrel(N):
    Cache = empty_assoc()
    Seeds = []
    Related = []
    Palindromes = []
    lychrel(N, 1, Cache, Seeds, Related, Palindromes)
    Num_seeds = len(Seeds)
    Num_related = len(Related)
    print('number of seeds:', Num_seeds)
    print('seeds:', Seeds)
    print('number of related:', Num_related)
    print('palindromes:', Palindromes)

def main():
    lychrel(10000)