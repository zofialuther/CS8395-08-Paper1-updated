def flatten(List, FlatList):
    def inner_flatten(Var, T, FlatList):
        if isinstance(Var, list):
            for i in Var:
                inner_flatten(i, T, FlatList)
        else:
            FlatList.append(Var)
    
    inner_flatten(List, [], FlatList)