def is_leap_year(year):
    return not year % (4 if year % 100 != 0 else 400)