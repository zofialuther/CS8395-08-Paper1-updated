def bin_search(Elt, List, Result):
    N = len(List)
    bin_search_inner(Elt, List, 1, N, Result)

def bin_search_inner(Elt, List, Begin, End, Result):
    if Begin == End:
        Result = List[Begin]
    else:
        if Begin < End:
            Mid = (Begin + End) // 2
            Result = List[Mid]
        elif Begin < End:
            Mid = (Begin + End) // 2
            MidElt = List[Mid]
            if MidElt < Elt:
                NewBegin = Mid + 1
                bin_search_inner(Elt, List, NewBegin, End, Result)
            elif Begin < End:
                Mid = (Begin + End) // 2
                MidElt = List[Mid]
                if MidElt > Elt:
                    NewEnd = Mid - 1
                    bin_search_inner(Elt, List, Begin, NewEnd, Result)