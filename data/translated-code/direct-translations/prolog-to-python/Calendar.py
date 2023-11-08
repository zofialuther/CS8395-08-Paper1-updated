```python
def write_calendar(Year):
    F1_3 = month_x3_format(Year, 1, 2, 3)
    F4_6 = month_x3_format(Year, 4, 5, 6)
    F7_9 = month_x3_format(Year, 7, 8, 9)
    F10_12 = month_x3_format(Year, 10, 11, 12)

    print('''
                                      {}

            January                  February                   March
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
{}

             April                     May                      June
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
{}

              July                    August                  September
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
{}

            October                  November                 December
      Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa     Su Mo Tu We Th Fr Sa
{}	
'''.format(Year, F1_3, F4_6, F7_9, F10_12))


def month_x3_format(Year, M1, M2, M3):
    M1r = calc_month_rows(Year, M1)
    M2r = calc_month_rows(Year, M2)
    M3r = calc_month_rows(Year, M3)
    return month_x3_format_helper(M1r, M2r, M3r)


def month_x3_format_helper(M1, M2, M3):
    if all(map(lambda x: x == '   ', M1)) and all(map(lambda x: x == '   ', M2)) and all(map(lambda x: x == '   ', M3)):
        return ''
    else:
        F1 = month_format('      ', M1)
        F2 = month_format(F1, M2)
        F3 = month_format(F2, M3)
        F4 = F3 + '\n'
        Fr = month_x3_format_helper(M1, M2, M3)
        return F4 + Fr


def month_format(Orig, M):
    Formatted = list(map(day_format, M))
    F2 = ''.join(Formatted) + '    '
    return Orig + F2


def day_format(D):
    if D == '   ':
        return '   '
    elif D < 10:
        return f'{D}  '
    else:
        return f'{D} '


def calc_month_rows(Year, Month):
    Result = []
    DaysInMonth = month_days(Month, Year)
    FirstWeekDay = day_of_the_week(date(Year, Month, 1))
    Offset = day_offset(FirstWeekDay)
    day_print_map(DaysInMonth, Offset, Result)
    return Result


def day_print_map(DaysInMonth, Offset, Result):
    if Offset == 0:
        Result.append(1)
        day_print_map2(DaysInMonth, 2, Result)
    elif Offset != 0:
        Offset += 1
        Result.append('   ')
        day_print_map(DaysInMonth, Offset, Result)


def day_print_map2(D, N, Result):
    if D == N:
        Result.append(N)
    elif D != N:
        N += 1
        Result.append(N)
        day_print_map2(D, N, Result)


def month_days(Month, Year):
    if Month == 2:
        if is_leap_year(Year):
            return 29
        else:
            return 28
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][Month-1]


def day_offset(D):
    if D != 7:
        return D
    else:
        return 0


def is_leap_year(Year):
    if Year % 100 == 0:
        return Year % 400 == 0
    else:
        return Year % 4 == 0
```