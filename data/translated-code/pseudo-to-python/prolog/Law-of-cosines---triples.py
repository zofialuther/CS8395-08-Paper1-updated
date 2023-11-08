def find_solutions(Limit, Solutions):
    find_solutions(Limit, Solutions, Limit, [])

def find_solutions(_, S, 0, S):
    return
def find_solutions(Limit, Solutions, A, S):
    find_solutions1(Limit, A, A, [], S1)
    A_next = A - 1
    find_solutions(Limit, Solutions, A_next, S1)

def find_solutions1(Limit, _, B, Triples, Triples):
    if B > Limit:
        return
def find_solutions1(Limit, A, B, [Triple|Triples], T):
    if is_solution(Limit, A, B, Triple):
        B_next = B + 1
        find_solutions1(Limit, A, B_next, Triples, T)
    else:
        B_next = B + 1
        find_solutions1(Limit, A, B_next, Triples, T)

def is_solution(Limit, A, B, t(Angle, A, B, C)):
    X = A * A + B * B
    Y = A * B
    if Angle == 90:
        C = round(X ** 0.5)
        if X == C * C and C <= Limit:
            return
    elif Angle == 120:
        C2 = X + Y
        C = round(C2 ** 0.5)
        if C2 == C * C and C <= Limit:
            return
    elif Angle == 60:
        C2 = X - Y
        C = round(C2 ** 0.5)
        if C2 == C * C and C <= Limit:
            return

def write_triples(Angle, Solutions):
    find_triples(Angle, Solutions, [], 0, 0)
    write_triples1(List)
    print()

def find_triples(_, [], [], Count, Count):
    return
def find_triples(Angle, [Triple|Triples], [Triple|Result], C, Count):
    if Triple[0] == Angle:
        C1 = C + 1
        find_triples(Angle, Triples, Result, C1, Count)
def find_triples(Angle, [_|Triples], Result, C, Count):
    find_triples(Angle, Triples, Result, C, Count)

def write_triples1([]):
    return
def write_triples1([t(_, A, B, C)]):
    print(f'({A},{B},{C})')
    return
def write_triples1([t(_, A, B, C), *Triples]):
    print(f'({A},{B},{C})', end=" ")
    write_triples1(Triples)

def main():
    Solutions = []
    find_solutions(13, Solutions)
    write_triples(60, Solutions)
    write_triples(90, Solutions)
    write_triples(120, Solutions)

main()