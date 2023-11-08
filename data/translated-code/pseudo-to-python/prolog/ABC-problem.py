def abc_problem():
    words = ['', 'A', 'bark', 'bOOk', 'treAT', 'COmmon', 'sQuaD', 'CONFUSE']
    for word in words:
        abc_problem(word)

def abc_problem(Word):
    L = [['b', 'o'], ['x', 'k'], ['d', 'q'], ['c', 'p'], ['n', 'a'], ['g', 't'], 
         ['r', 'e'], ['t', 'g'], ['q', 'd'], ['f', 's'], ['j', 'w'], ['h', 'u'], 
         ['v', 'i'], ['a', 'n'], ['o', 'b'], ['e', 'r'], ['f', 's'], ['l', 'y'], 
         ['p', 'c'], ['z', 'm']]
    if abc_problem_helper(L, Word):
        print(f'{Word} OK')
    else:
        print(f'{Word} KO')

def abc_problem_helper(L, Word):
    C_Words = list(Word)
    D_Words = list(map(str.lower, C_Words))
    return can_makeword(L, D_Words)

def can_makeword(_L, T):
    if len(T) == 0:
        return True
    else:
        H, *rest = T
        for pair in _L:
            if pair[0] == H or pair[1] == H:
                new_L = [x for x in _L if x != pair]
                if can_makeword(new_L, rest):
                    return True
        return False