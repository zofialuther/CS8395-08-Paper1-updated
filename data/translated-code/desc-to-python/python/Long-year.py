import datetime

def longYear(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    num_weeks = (end_date - start_date).days // 7
    return num_weeks == 53

def main():
    long_years = [year for year in range(2000, 2101) if longYear(year)]
    print(long_years)

main()