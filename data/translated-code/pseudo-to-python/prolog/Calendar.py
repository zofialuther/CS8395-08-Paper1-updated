```python
def write_calendar(Year):
    month_x3_format(Year, 1, 2, 3, F1_3)
    month_x3_format(Year, 4, 5, 6, F4_6)
    month_x3_format(Year, 7, 8, 9, F7_9)
    month_x3_format(Year, 10, 11, 12, F10_12)

    print(FORMAT('

                                      ~w

            January                  February                   March
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
~w

             April                     May                      June
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
~w

              July                    August                  September
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
~w

            October                  November                 December
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
~w   
', [Year, F1_3, F4_6, F7_9, F10_12]))

def month_x3_format(Year, M1, M2, M3, F):
    M1r = calc_month_rows(Year, M1)
    M2r = calc_month_rows(Year, M2)
    M3r = calc_month_rows(Year, M3)
    F = month_x3_format(M1r, M2r, M3r)

def month_x3_format(M1, M2, M3, F):
    if maplist(=('   '), M1) and maplist(=('   '), M2) and maplist(=('   '), M3):
        return ''
    else:
        F1 = month_format('      ', M1)
        F2 = month_format(F1, M2)
        F3 = month_format(F2, M3)
        F4 = F3 + '\n'
        Fr = month_x3_format(M1r, M2r, M3r)
        return F4 + Fr

def month_format(Orig, [Su, Mo, Tu, We, Th, Fr, Sa | R], R, F):
    Formatted = maplist(day_format, [Su, Mo, Tu, We, Th, Fr, Sa])
    F2 = FORMAT('~w~w~w~w~w~w~w    ', Formatted)
    F = Orig + F2

def day_format('   ', '  '):
    return

def day_format(D, F):
    if D < 10:
        F = FORMAT('~w  ', D)
    else:
        F = FORMAT('~w ', D)

def calc_month_rows(Year, Month, Result):
    Result = [None]*42
    DaysInMonth = month_days(Month, Year)
    FirstWeekDay = day_of_the_week(date(Year, Month, 1))
    Offset = day_offset(FirstWeekDay)
    Result = day_print_map(DaysInMonth, Offset)

def day_print_map(DaysInMonth, 0, [1 | R]):
    return day_print_map2(DaysInMonth, 2, R)

def day_print_map(DaysInMonth, Offset, ['   ' | R]):
    if dif(Offset, 0):
        NewOffset = Offset + 1
        return day_print_map(DaysInMonth, NewOffset, R)

def day_print_map2(D, D, [D | R]):
    return day_print_map(R)
def day_print_map2(D, N, [N | R]):
    if dif(D, N):
        N1 = N + 1
        return day_print_map2(D, N1, R)

def month_days(2, Year, Days):
    if is_leap_year(Year):
        Days = 29
    else:
        Days = 28
def month_days(Month, _, Days):
    if dif(Month, 2):
        Days = nth1(Month, [31, _, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

def day_offset(D, D):
    if dif(D, 7):
        return D
def day_offset(7, 0):
    return 0

def is_leap_year(Year):
    if 0 is Year % 100:
        if 0 is Year % 400:
            return True
        else:
            return False
    else:
        if 0 is Year % 4:
            return True
        else:
            return False
```