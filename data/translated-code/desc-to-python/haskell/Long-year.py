import datetime
import calendar

def longYear(year):
    jan_1 = datetime.date(year, 1, 1)
    dec_31 = datetime.date(year, 12, 31)
    return (jan_1.isocalendar()[1] == 1 and dec_31.isocalendar()[1] == 53)

def main():
    long_years = [year for year in range(2000, 2101) if longYear(year)]
    print(long_years)

main()