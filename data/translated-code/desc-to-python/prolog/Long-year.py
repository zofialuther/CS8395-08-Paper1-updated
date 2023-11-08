def is_long_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 3 and year % 100 != 3):
        return True
    else:
        return False

def print_long_years(start_year, end_year):
    for year in range(start_year, end_year+1):
        if is_long_year(year):
            print(year)

print_long_years(1800, 2100)