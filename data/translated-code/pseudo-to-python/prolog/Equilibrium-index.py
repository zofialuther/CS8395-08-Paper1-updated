def equilibrium_index(List, Index):
    Front = []
    Back = []
    
    for i in range(1, len(List)):
        Front.append(List[i-1])
        Back = List[i:]
        
        SumFront = sum(Front)
        SumBack = sum(Back)
        
        if SumFront == SumBack:
            Index = len(Front)
            return
        
    Index = -1