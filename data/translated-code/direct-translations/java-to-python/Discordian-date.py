import java.util.Calendar

seasons = ["Chaos", "Discord", "Confusion", "Bureaucracy", "The Aftermath"]
weekday = ["Sweetmorn", "Boomtime", "Pungenday", "Prickle-Prickle", "Setting Orange"]
apostle = ["Mungday", "Mojoday", "Syaday", "Zaraday", "Maladay"]
holiday = ["Chaoflux", "Discoflux", "Confuflux", "Bureflux", "Afflux"]

def discordianDate(date):
    y = date.get(Calendar.YEAR)
    yold = y + 1166
    dayOfYear = date.get(Calendar.DAY_OF_YEAR)

    if (date.isLeapYear(y)):
        if (dayOfYear == 60):
            return "St. Tib's Day, in the YOLD " + yold
        elif (dayOfYear > 60):
            dayOfYear -= 1

    dayOfYear -= 1

    seasonDay = dayOfYear % 73 + 1
    if (seasonDay == 5):
        return apostle[dayOfYear // 73] + ", in the YOLD " + yold
    if (seasonDay == 50):
        return holiday[dayOfYear // 73] + ", in the YOLD " + yold

    season = seasons[dayOfYear // 73]
    dayOfWeek = weekday[dayOfYear % 5]

    return "%s, day %s of %s in the YOLD %s" % (dayOfWeek, seasonDay, season, yold)

def test(y, m, d, result):
    assert(discordianDate(Calendar(y, m, d)) == result)

test(2010, 6, 22, "Pungenday, day 57 of Confusion in the YOLD 3176")
test(2012, 1, 28, "Prickle-Prickle, day 59 of Chaos in the YOLD 3178")
test(2012, 1, 29, "St. Tib's Day, in the YOLD 3178")
test(2012, 2, 1, "Setting Orange, day 60 of Chaos in the YOLD 3178")
test(2010, 0, 5, "Mungday, in the YOLD 3176")
test(2011, 4, 3, "Discoflux, in the YOLD 3177")
test(2015, 9, 19, "Boomtime, day 73 of Bureaucracy in the YOLD 3181")