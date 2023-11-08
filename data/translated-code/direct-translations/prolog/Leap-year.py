def leap_year(L):
    LIn = [year for year in L if is_leap_year(year)]
    LOut = [year for year in L if not is_leap_year(year)]
    print('leap years :', LIn)
    print('not leap years :', LOut)

def is_leap_year(year):
    R4 = year % 4
    R100 = year % 100
    R400 = year % 400
    return (R4 == 0 and R100 != 0) or R400 == 0