def isLeapYear(year):
    if year % 100 == 0:
        return (year % 400 == 0)
    else:
        return (year % 4 == 0)

yrs = [1800,1900,1994,1998,1999,2000,2001,2004,2100]

for year in yrs:
    print("The year " + str(year) + " is leaper: " + str(isLeapYear(year)))