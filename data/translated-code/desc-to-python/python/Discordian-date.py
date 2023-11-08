```python
def calculate_discordian_date(year, month, day):
    seasons = ["Chaos", "Discord", "Confusion", "Bureaucracy", "The Aftermath"]
    season_day = 0
    
    if month == 1:
        season_day = day
    elif month == 2:
        season_day = 31 + day
    elif month == 3:
        season_day = 59 + day
    elif month == 4:
        season_day = 90 + day
    elif month == 5:
        season_day = 120 + day
    elif month == 6:
        season_day = 151 + day
    elif month == 7:
        season_day = 181 + day
    elif month == 8:
        season_day = 212 + day
    elif month == 9:
        season_day = 243 + day
    elif month == 10:
        season_day = 273 + day
    elif month == 11:
        season_day = 304 + day
    elif month == 12:
        season_day = 334 + day
        
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if month > 2:
            season_day += 1

    if season_day == 60:
        discordian_date = "St. Tib's Day, YOLD " + str(year)
    else:
        season_index = (season_day - 1) // 73
        day_of_season = (season_day - 1) % 73 + 1
        discordian_date = seasons[season_index] + " " + str(day_of_season) + ", YOLD " + str(year)
    
    return discordian_date
```