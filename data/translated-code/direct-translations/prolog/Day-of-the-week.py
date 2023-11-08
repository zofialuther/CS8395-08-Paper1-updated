def main():
    sunday_list = christmas_days_falling_on_sunday(2011, 2121)
    print(sunday_list)

def christmas_days_falling_on_sunday(start_year, end_year):
    year_range_list = list(range(start_year, end_year + 1))
    sunday_list = list(filter(is_christmas_day_a_sunday, year_range_list))
    return sunday_list

def is_christmas_day_a_sunday(year):
    import datetime
    date = datetime.date(year, 12, 25)
    day_of_the_week = date.weekday() + 1
    return day_of_the_week == 7

main()