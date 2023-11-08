def look_and_say(L):
    for element in L:
        print(element)
    print("\n")
    L1 = encode(L)
    look_and_say(L1)

def encode(In):
    Out = []
    R1 = packList(In)
    Out.append(R1)
    return Out

def packList(In):
    if not In:
        return []
    elif len(In) == 1:
        return [[1, In[0]]]
    else:
        X = In[0]
        Rest = In[1:]
        XRun = run(X, Rest)
        Packed = packList(Rest)
        return [XRun] + Packed

def run(Var, LRest):
    if not LRest:
        return [1, Var]
    elif LRest[0] == Var:
        return [1 + LRest[0]] + [Var]
    elif LRest[0] != Var:
        return [1, Var] + LRest[1:]