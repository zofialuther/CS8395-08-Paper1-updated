from datetime import datetime, timedelta

years = [False] * 201
month31 = [1, 3, 5, 7, 8, 10, 12]

def main():
    months = ""
    numMonths = 0
    for year in range(1900, 2101):
        for month in month31:
            date = datetime(year, month, 1)
            if date.weekday() == 4:
                years[year - 1900] = True
                numMonths += 1
                months += str(date.month) + "-" + str(year) + "\n"
    print("There are " + str(numMonths) + " months with five weekends from 1900 through 2100:")
    print(months)
    print("Years with no five-weekend months:")
    for year in range(1900, 2101):
        if not years[year - 1900]:
            print(year)

if __name__ == "__main__":
    main()