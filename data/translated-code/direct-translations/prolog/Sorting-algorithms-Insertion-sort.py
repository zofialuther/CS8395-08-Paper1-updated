def insert_sort(L1, L2):
    insert_sort_intern(L1, [], L2)

def insert_sort_intern([], L, L):
    pass

def insert_sort_intern([H|T], L1, L):
    L2 = insert(L1, H)
    insert_sort_intern(T, L2, L)

def insert([], X, [X]):
    pass

def insert([H|T], X, [X,H|T]):
    if X <= H:
        return
    else:
        insert(T, X, T2)