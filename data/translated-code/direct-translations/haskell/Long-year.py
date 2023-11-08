from datetime import datetime

def longYear(y):
    date = datetime(y, 12, 28)
    week_number = date.isocalendar()[1]
    return week_number > 52

if __name__ == "__main__":
    for year in range(2000, 2101):
        if longYear(year):
            print(year)