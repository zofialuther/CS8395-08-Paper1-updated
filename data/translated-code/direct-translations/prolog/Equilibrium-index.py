def equilibrium_index(List, Index):
    for i in range(len(List)):
        front = List[:i]
        back = List[i+1:]
        if sum(front) == sum(back):
            Index = i
            break