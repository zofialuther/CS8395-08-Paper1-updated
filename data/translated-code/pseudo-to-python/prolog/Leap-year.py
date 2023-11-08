def leap_year(L):
    LIn = []
    LOut = []
    for i in range(len(L)):
        if is_leap_year(L[i]):
            LIn.append(L[i])
        else:
            LOut.append(L[i])
    print('leap years : ', LIn)
    print('not leap years : ', LOut)

def is_leap_year(Year):
    R4 = Year % 4
    R100 = Year % 100
    R400 = Year % 400
    if (R4 == 0 and R100 != 0) or R400 == 0:
        return True
    else:
        return False