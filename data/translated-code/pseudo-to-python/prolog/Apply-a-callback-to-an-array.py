def fun(X):
    return 2 * X

def maplist(fun, List):
    Result = []
    for element in List:
        Result.append(fun(element))
    return Result