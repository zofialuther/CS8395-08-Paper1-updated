def a_to_z(From, To, L):
    C_From = ord(From)
    C_To = ord(To)
    L1 = []
    for C in range(C_From, C_To + 1):
        L1.append(chr(C))
    L = list(map(ord, L1))