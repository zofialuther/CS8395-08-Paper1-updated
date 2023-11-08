```python
import datetime

def long_year(year):
    first_day = datetime.date(year, 1, 1)
    last_day = datetime.date(year, 12, 31)
    if last_day.isocalendar()[1] == 53:
        return True
    else:
        return False

def main():
    for year in range(2000, 2100):
        if long_year(year):
            print(year)

if __name__ == "__main__":
    main()
```