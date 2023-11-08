from datetime import datetime, timedelta

def long_year(year):
    date = datetime(year, 12, 28)
    week_number = date.isocalendar()[1]
    return week_number == 53

print("Long years this century:")
for year in range(2000, 2100):
    if long_year(year):
        print(year, end=" ")