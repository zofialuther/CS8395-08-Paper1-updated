def odd_word_problem(user_input):
    L = read_line_to_codes(user_input)
    Out = even_word(L, [])
    Str = string_to_list(Out)
    print(Str)

def even_word(L, Acc):
    return even_word_helper(L, Acc, [])

def even_word_helper(L, Acc, Result):
    if L == ".":
        return Acc
    else:
        if L[0].isalnum():
            NewAcc = Acc + [L[0]]
            return even_word_helper(L[1:], NewAcc, Result)
        else:
            return even_word_helper(L[1:], Acc, Result)

def odd_word(L, R):
    return odd_word_helper(L, R, [])

def odd_word_helper(L, R, Result):
    if L == ".":
        return R
    else:
        if L[0].isalnum():
            NewR = [L[0]] + R
            return odd_word_helper(L[1:], NewR, Result)
        else:
            NewR = R + [L[0]]
            return even_word(L[1:], [], NewR)