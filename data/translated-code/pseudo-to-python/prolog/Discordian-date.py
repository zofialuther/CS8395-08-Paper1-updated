def main():
    test(2022, 4, 20)
    test(2020, 5, 24)
    test(2020, 2, 29)
    test(2019, 7, 15)
    test(2025, 3, 19)
    test(2017, 12, 8)

def test(Gregorian_year, Gregorian_month, Gregorian_day):
    Discordian_date = ddate(Gregorian_year, Gregorian_month, Gregorian_day)
    print(f'{Gregorian_year}/{Gregorian_month}/{Gregorian_day} converts to {Discordian_date}')

def ddate(Gregorian_year, Gregorian_month, Gregorian_day):
    Discordian_year = convert_year(Gregorian_year)
    Daynum = day_of_year(Gregorian_month, Gregorian_day)
    Season = Daynum // 73
    Weekday = Daynum % 5
    Day_of_season = 1 + Daynum % 73
    Season_name = season(Season)
    Day_name = week_day(Weekday)
    Holy_day = holy_day(Season, Day_of_season)
    if Holy_day:
        return f'{Day_name}, {Day_of_season} {Season_name} {Discordian_year}, {Holy_day}'
    else:
        return f'{Day_name}, {Day_of_season} {Season_name} {Discordian_year}'

def convert_year(Gregorian_year):
    return Gregorian_year + 1166

def day_of_year(M, D):
    Days = month_days(M)
    return Days + D - 1

def month_days(M):
    if M == 1:
        return 0
    # other month_days definitions

def season(Season):
    if Season == 0:
        return 'Chaos'
    # other season definitions

def week_day(Weekday):
    if Weekday == 0:
        return 'Sweetmorn'
    # other week_day definitions

def holy_day(Season, Day_of_season):
    if Season == 0 and Day_of_season == 5:
        return 'Mungday'
    # other holy_day definitions