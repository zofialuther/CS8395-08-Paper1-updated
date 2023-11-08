def isXmasSunday(year):
    weekDay = datetime.date(year, 12, 25).weekday()
    return weekDay == 6

def main():
    for year in range(2008, 2122):
        if isXmasSunday(year):
            print("Sunday 25 December " + str(year))

main()