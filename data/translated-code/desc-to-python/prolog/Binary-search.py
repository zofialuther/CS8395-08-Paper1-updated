```python
def bin_search(Elt, List, Result):
    length = len(List)
    bin_search_inner(Elt, List, 0, length-1, Result)

def bin_search_inner(Elt, List, Start, End, Result):
    if Start > End:
        Result = -1
    else:
        Mid = (Start + End) // 2
        if List[Mid] == Elt:
            Result = Mid
        elif List[Mid] < Elt:
            bin_search_inner(Elt, List, Mid+1, End, Result)
        else:
            bin_search_inner(Elt, List, Start, Mid-1, Result)
```