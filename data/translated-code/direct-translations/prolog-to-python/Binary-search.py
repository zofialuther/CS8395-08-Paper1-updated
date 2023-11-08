def bin_search(Elt, List, Result):
    N = len(List)
    bin_search_inner(Elt, List, 1, N, Result)

def bin_search_inner(Elt, List, J, J, J):
    return List[J] == Elt

def bin_search_inner(Elt, List, Begin, End, Mid):
    if Begin < End:
        Mid = (Begin + End) // 2
        return List[Mid] == Elt
    elif List[Mid] < Elt:
        NewBegin = Mid + 1
        return bin_search_inner(Elt, List, NewBegin, End, Result)
    elif List[Mid] > Elt:
        NewEnd = Mid - 1
        return bin_search_inner(Elt, List, Begin, NewEnd, Result)