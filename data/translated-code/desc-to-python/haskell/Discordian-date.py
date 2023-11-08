```python
from datetime import datetime

def fromYMD(year, month, day):
    return datetime(year, month, day).strftime('%B %d, %Y')

def display(date):
    formatted_date = fromYMD(date[0], date[1], date[2])
    print(f"{formatted_date} - {date[1]}/{date[2]}/{date[0]}")

dates = [(2020, 1, 15), (2021, 2, 28), (2024, 12, 25)]
mapM_(display, dates)
```