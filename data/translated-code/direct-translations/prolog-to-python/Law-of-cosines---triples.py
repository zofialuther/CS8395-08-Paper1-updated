def find_solutions(limit, solutions):
    find_solutions(limit, solutions, limit, [])

def find_solutions(limit, solutions, a, s):
    if a == 0:
        return
    else:
        s1 = find_solutions1(limit, a, a, [], s)
        a_next = a - 1
        find_solutions(limit, solutions, a_next, s1)

def find_solutions1(limit, a, b, triples, t):
    if b > limit:
        return
    else:
        if is_solution(limit, a, b, triple):
            b_next = b + 1
            find_solutions1(limit, a, b_next, triples, t)
        else:
            b_next = b + 1
            find_solutions1(limit, a, b_next, triples, t)

def is_solution(limit, a, b, triple):
    x = a * a + b * b
    y = a * b
    if angle == 90:
        c = round(sqrt(x))
        if x == c * c and c <= limit:
            return True
    elif angle == 120:
        c2 = x + y
        c = round(sqrt(c2))
        if c2 == c * c and c <= limit:
            return True
    elif angle == 60:
        c2 = x - y
        c = round(sqrt(c2))
        if c2 == c * c and c <= limit:
            return True
    else:
        return False

def write_triples(angle, solutions):
    list = []
    count = 0
    find_triples(angle, solutions, list, 0, count)
    print(f'There are {count} solutions for gamma = {angle}:')
    write_triples1(list)
    print()

def find_triples(angle, triples, result, c, count):
    if not triples:
        return
    else:
        if triple.angle == angle:
            c += 1
            find_triples(angle, triples[1:], result, c, count)
        else:
            find_triples(angle, triples[1:], result, c, count)

def write_triples1(triples):
    if not triples:
        return
    else:
        print(f'({triples[0].a},{triples[0].b},{triples[0].c})')
        write_triples1(triples[1:])

def main():
    solutions = []
    find_solutions(13, solutions)
    write_triples(60, solutions)
    write_triples(90, solutions)
    write_triples(120, solutions)

main()