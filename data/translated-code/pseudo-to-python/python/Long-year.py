def longYear(y):
    return 52 < datetime.date(y, 12, 28).isocalendar()[1]

def main():
    for year in [x for x in range(2000, 2101) if longYear(x)]:
        print(year)