def odd_word_problem():
    L = input()
    Out = even_word(L, [], [])
    Str = ''.join(Out)
    print(Str)

def even_word(L, Out, _):
    if L == ".":
        Out.append(".")
    else:
        if L[0].isalnum():
            Out.append(L[0])
            even_word(L[1:], Out, [])
        else:
            even_word(L[1:], Out, [])
    return Out

def odd_word(L, R):
    if L == ".":
        return R + "."
    else:
        if L[0].isalnum():
            R.append(L[0])
            return odd_word(L[1:], R)
        else:
            return R + L[0] + even_word(L[1:], [], [])

odd_word_problem()