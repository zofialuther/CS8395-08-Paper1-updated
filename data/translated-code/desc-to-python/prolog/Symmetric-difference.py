def sym_diff(A, B):
    set_A = set(A)
    set_B = set(B)
    
    diff_A_B = set_A.difference(set_B)
    diff_B_A = set_B.difference(set_A)
    
    sym_diff = diff_A_B.union(diff_B_A)
    print(sym_diff)