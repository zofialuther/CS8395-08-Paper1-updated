def abc_problem():
    words = ['', 'A', 'bark', 'bOOk', 'treAT', 'COmmon', 'sQuaD', 'CONFUSE']
    for word in words:
        abc_problem(word)

def abc_problem(word):
    L = [['b', 'o'], ['x', 'k'], ['d', 'q'], ['c', 'p'], ['n', 'a'], ['g', 't'], ['r', 'e'], ['t', 'g'], ['q', 'd'], ['f', 's'],
         ['j', 'w'], ['h', 'u'], ['v', 'i'], ['a', 'n'], ['o', 'b'], ['e', 'r'], ['f', 's'], ['l', 'y'], ['p', 'c'], ['z', 'm']]

    if abc_problem_helper(L, word):
        print(word + " OK")
    else:
        print(word + " KO")

def abc_problem_helper(L, word):
    c_words = list(word)
    d_words = [c_word.lower() for c_word in c_words]
    return can_make_word(L, d_words)

def can_make_word(L, words):
    if len(words) == 0:
        return True
    else:
        head = words[0]
        tail = words[1:]
        for pair in L:
            if pair[0] == head or pair[1] == head:
                new_L = [x for x in L if x != pair]
                return can_make_word(new_L, tail)

abc_problem()