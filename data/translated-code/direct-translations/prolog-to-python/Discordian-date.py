```python
# See https://en.wikipedia.org/wiki/Discordian_calendar

def main():
    test(2022, 4, 20)
    test(2020, 5, 24)
    test(2020, 2, 29)
    test(2019, 7, 15)
    test(2025, 3, 19)
    test(2017, 12, 8)

def test(Gregorian_year, Gregorian_month, Gregorian_day):
    Discordian_date = ddate(Gregorian_year, Gregorian_month, Gregorian_day)
    print(f"{Gregorian_year:02d}-{Gregorian_month:02d}-{Gregorian_day:02d}: {Discordian_date}")

def ddate(Gregorian_year, Gregorian_month, Gregorian_day):
    if Gregorian_month == 2 and Gregorian_day == 29:
        Discordian_year = convert_year(Gregorian_year)
        Discordian_date = f"St. Tib's Day in the YOLD {Discordian_year}"
    else:
        Discordian_year = convert_year(Gregorian_year)
        Daynum = day_of_year(Gregorian_month, Gregorian_day)
        Season = Daynum // 73
        Weekday = Daynum % 5
        Day_of_season = 1 + Daynum % 73
        Season_name = season(Season)
        Day_name = week_day(Weekday)
        if holy_day(Season, Day_of_season):
            Holy_day = holy_day(Season, Day_of_season)
            Discordian_date = f"{Day_name}, day {Day_of_season} of {Season_name} in the YOLD {Discordian_year}. Celebrate {Holy_day}!"
        else:
            Discordian_date = f"{Day_name}, day {Day_of_season} of {Season_name} in the YOLD {Discordian_year}"
    return Discordian_date

def convert_year(Gregorian_year):
    return Gregorian_year + 1166

def day_of_year(M, D):
    Days = month_days(M)
    return Days + D - 1

def month_days(month):
    if month == 1:
        return 0
    elif month == 2:
        return 31
    elif month == 3:
        return 59
    elif month == 4:
        return 90
    elif month == 5:
        return 120
    elif month == 6:
        return 151
    elif month == 7:
        return 181
    elif month == 8:
        return 212
    elif month == 9:
        return 243
    elif month == 10:
        return 273
    elif month == 11:
        return 304
    elif month == 12:
        return 334

def season(num):
    if num == 0:
        return 'Chaos'
    elif num == 1:
        return 'Discord'
    elif num == 2:
        return 'Confusion'
    elif num == 3:
        return 'Bureacracy'
    elif num == 4:
        return 'The Aftermath'

def week_day(num):
    if num == 0:
        return 'Sweetmorn'
    elif num == 1:
        return 'Boomtime'
    elif num == 2:
        return 'Pungenday'
    elif num == 3:
        return 'Prickle-Prickle'
    elif num == 4:
        return 'Setting Orange'

def holy_day(season, day_of_season):
    if (season == 0 and day_of_season == 5) or (season == 0 and day_of_season == 50):
        return 'Mungday' if day_of_season == 5 else 'Chaoflux'
    elif (season == 1 and day_of_season == 5) or (season == 1 and day_of_season == 50):
        return 'Mojoday' if day_of_season == 5 else 'Discoflux'
    elif (season == 2 and day_of_season == 5) or (season == 2 and day_of_season == 50):
        return 'Syaday' if day_of_season == 5 else 'Confuflux'
    elif (season == 3 and day_of_season == 5) or (season == 3 and day_of_season == 50):
        return 'Zaraday' if day_of_season == 5 else 'Bureflux'
    elif (season == 4 and day_of_season == 5) or (season == 4 and day_of_season == 50):
        return 'Maladay' if day_of_season == 5 else 'Afflux'

main()
```