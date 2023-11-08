from datetime import datetime

def long_year(year):
    if datetime(year, 12, 28).isocalendar()[1] == 53:
        return True
    else:
        return False

print("Long years this century:")
for year in range(2000, 2100):
    if long_year(year):
        print(year)