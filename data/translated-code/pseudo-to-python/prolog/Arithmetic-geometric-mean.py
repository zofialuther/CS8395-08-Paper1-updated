def agm(A, G, Res):
    if abs(A - G) < 1.0e-15:
        Res = (A + G) / 2.0
    else:
        A1 = (A + G) / 2.0
        G1 = (A * G) ** 0.5
        agm(A1, G1, Res)

agm(1, 1/(2 ** 0.5), Res)
print(Res) # Output: 0.8472130847939792