def a_to_z(From, To, L):
    C_From = ord(From)
    C_To = ord(To)
    L1 = [chr(c) for c in range(C_From, C_To + 1)]
    L = ["".join(c) for c in L1]