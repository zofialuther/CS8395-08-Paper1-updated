def van_eck_init(v):
    v = {}
    return v

def van_eck_next(Index, Last_term, Last_pos, Index1, Next_term, Last_pos1):
    if Last_term in Last_pos:
        V = Last_pos[Last_term]
        Next_term = Index - V
    else:
        Next_term = 0
    Index1 = Index + 1
    Last_pos1[Last_term] = Index
    return Index1, Next_term, Last_pos1

def van_eck_sequence(N, Seq):
    V = van_eck_init({})
    van_eck_sequence_recursive(N, V, Seq)

def van_eck_sequence_recursive(N, V, Seq):
    if N == 0:
        return
    else:
        V = (_, Seq[-1], _)
        Index, Next_term, Last_pos = van_eck_next(Seq[-1], V[1], V[2], _, _, {})
        N1 = N - 1
        Seq.append(Next_term)
        van_eck_sequence_recursive(N1, (Index, Next_term, Last_pos), Seq)

def write_list(From, To, N, List):
    if To < From:
        return
    else:
        if len(List) == 0:
            return
        else:
            if From > N:
                N1 = N + 1
                write_list(From, To, N1, List[1:])
            else:
                print(List[0], end=' ')
                F1 = From + 1
                N1 = N + 1
                write_list(F1, To, N1, List[1:])

def main():
    Seq = []
    van_eck_sequence(1000, Seq)
    print('First 10 terms of the Van Eck sequence:')
    write_list(1, 10, 1, Seq)
    print('\nTerms 991 to 1000 of the Van Eck sequence:')
    write_list(991, 1000, 1, Seq)