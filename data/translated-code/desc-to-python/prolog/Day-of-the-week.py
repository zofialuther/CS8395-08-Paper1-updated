from datetime import date

def is_christmas_day_a_sunday(year):
    christmas_date = date(year, 12, 25)
    return christmas_date.weekday() == 6

def christmas_days_falling_on_sunday():
    years = [year for year in range(2011, 2122) if is_christmas_day_a_sunday(year)]
    return years

def main():
    years_with_christmas_on_sunday = christmas_days_falling_on_sunday()
    for year in years_with_christmas_on_sunday:
        print(year)

main()