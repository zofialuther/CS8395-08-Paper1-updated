def puzzle():
    L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 12):
        L[i] = 1
    A2 = (L[6] + L[7] + L[8] + L[9] + L[10] + L[11])
    A3 = (A2 + L[3] + L[5] + L[7] + L[9] + L[11])
    A4 = (L[4] >= (L[5] and L[6]))
    A5 = (A2 + A3 + A4)
    A6 = (L[0] + A3 + A5 + L[6] + L[8] + L[10])
    A7 = (A2 + A3)
    A8 = (A7 >=  (A5 and A6))
    A9 = (L[0] + A2 + A3 + A4 + A5 + A6)
    A10 = (L[11] and L[12])
    A11 = (A7 + A8 + A9)
    A12 = (L[0] + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11)
    
    for i in range(0, 12):
        print('Statement ' + str(i+1) + ' is ' + str(L[i]))