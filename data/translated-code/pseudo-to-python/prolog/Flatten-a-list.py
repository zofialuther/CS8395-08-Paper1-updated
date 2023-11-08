def flatten(List, FlatList):
    flattenHelper(List, [], FlatList)

def flattenHelper(Var, T, FlatList):
    if isinstance(Var, list):
        if len(Var) == 0:
            FlatList = T
        else:
            flattenHelper(Var[0], [], FlatTail)
            flattenHelper(Var[1:], FlatTail, FlatList)
    else:
        T.append(Var)
        FlatList = T