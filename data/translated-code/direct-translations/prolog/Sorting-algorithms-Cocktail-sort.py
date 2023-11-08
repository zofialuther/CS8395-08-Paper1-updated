```python
def ctail(_, [], Rev, Rev, sorted):
    print(Rev)
    print("\n")

def ctail(D, L, In, Rev, Ch):
    if D == "fwrd" and len(L) >= 2:
        A, B, *T = L
        if A > B:
            ctail("fwrd", [B, A, *T], In, Rev, "_")
    elif D == "bkwd" and len(L) >= 2:
        A, B, *T = L
        if A < B:
            ctail("bkwd", [B, A, *T], In, Rev, "_")
    elif len(L) >= 1:
        A, *T = L
        ctail(D, T, [A] + In, Rev, Ch)

def cocktail(In, Out):
    Rev = []
    Max = 0
    SFlag = ""
    if len(In) > 0:
        ctail("fwrd", In, [], Rev, SFlag)
        if SFlag == "sorted":
            Out = Rev[::-1]
        else:
            SortFlag = ""
            if len(Rev) > 0:
                ctail("bkwd", Rev, [Max], Out, SortFlag)
                if SortFlag != "sorted":
                    cocktail(Out, Out)

def test():
    In = [8, 9, 1, 3, 4, 2, 6, 5, 4]
    print("  input=", In)
    R = []
    cocktail(In, R)
    print("->", R)

test()
```