from datetime import date

def is_xmas_sunday(year):
    xmas_date = date(year, 12, 25)
    return xmas_date.weekday() == 6

def main():
    years = [year for year in range(2008, 2122) if is_xmas_sunday(year)]
    for year in years:
        print(f"Sunday 25 December {year}")

if __name__ == "__main__":
    main()