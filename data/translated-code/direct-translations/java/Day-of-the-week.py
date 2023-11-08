import datetime

def main():
    count = 1
    for year in range(2008, 2122):
        date = datetime.date(year, 12, 25)
        if date.weekday() == 6:  # 6 corresponds to Sunday
            if count != 1:
                print(", ", end="")
            print(year, end="")
            count += 1

if __name__ == "__main__":
    main()