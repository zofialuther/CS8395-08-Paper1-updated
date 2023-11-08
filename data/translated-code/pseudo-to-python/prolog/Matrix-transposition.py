def transpose(In, Out):
    if len(In) == 0:
        return
    else:
        H = In[0]
        T = In[1:]
        L = list(map(initdl, H))
        work(T, L, Out)

def initdl(V):
    return [V]

def work(Lst, H, Out):
    if len(H) == 1:
        Out = list(map(my_append_last, Lst, H))
    else:
        Lst1 = list(map(my_append, Lst, H[0]))
        work(Lst1, H[1:], Out)

def my_append(X, C):
    return X.append(C)

def my_append_last(X, C):
    return X.append(C)

def append_dl(X, Y):
    return X.append(Y)