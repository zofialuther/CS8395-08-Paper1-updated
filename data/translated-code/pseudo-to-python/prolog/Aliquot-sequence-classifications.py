def divisor_sum(N, Total):
    divisor_sum_prime(N, 2, 2, Total1, 1, N1)
    divisor_sum(N1, 3, Total, Total1)

def divisor_sum_1(_, Total, Total):
    return

def divisor_sum(N, Prime, Total, Running_total):
    if Prime * Prime <= N:
        divisor_sum_prime(N, Prime, Prime, P, 1, M)
        Next_prime = Prime + 2
        Running_total1 = P * Running_total
        divisor_sum(M, Next_prime, Total, Running_total1)
    else:
        Total = (N + 1) * Running_total

def divisor_sum_prime(N, Prime, Power, Total, Running_total, M):
    if N % Prime == 0:
        Running_total1 = Running_total + Power
        Power1 = Power * Prime
        N1 = N / Prime
        divisor_sum_prime(N1, Prime, Power1, Total, Running_total1, M)
    else:
        Total = Running_total

def aliquot_sequence(N, Limit, Sequence, Class):
    aliquot_sequence(N, Limit, [N], Sequence, Class)

def aliquot_sequence_1(_, 0, _, [], 'non-terminating'):
    return

def aliquot_sequence_2(_, _, [0|_], [0], terminating):
    return

def aliquot_sequence_3(N, _, [N, N|_], [], perfect):
    return

def aliquot_sequence_4(N, _, [N, _, N|_], [N], amicable):
    return

def aliquot_sequence_5(N, _, [N|S], [N], sociable):
    if N in S:
        pass

def aliquot_sequence_6(_, _, [Term, Term|_], [], aspiring):
    return

def aliquot_sequence_7(_, _, [Term|S], [Term], cyclic):
    if Term in S:
        pass

def aliquot_sequence(N, Limit, [Term|S], [Term|Rest], Class):
    divisor_sum(Term, Sum)
    Term1 = Sum - Term
    L1 = Limit - 1
    aliquot_sequence(N, L1, [Term1, Term|S], Rest, Class)

def write_aliquot_sequence(N, Sequence, Class):
    print(N, Class, "sequence:")
    write_aliquot_sequence(Sequence)

def write_aliquot_sequence_1([]):
    return

def write_aliquot_sequence_2([Term|Rest]):
    print(Term)
    write_aliquot_sequence(Rest)

def main():
    for N in range(1, 11):
        aliquot_sequence(N, 16, Sequence, Class)
        write_aliquot_sequence(N, Sequence, Class)
    for N in [11, 12, 28, 496, 220, 1184, 12496, 1264460, 790, 909, 562, 1064, 1488]:
        aliquot_sequence(N, 16, Sequence, Class)
        write_aliquot_sequence(N, Sequence, Class)