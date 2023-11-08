```python
from typing import List

def minimum_abbreviation_length(day_names: List[str], min_length: int):
    day_names.sort()
    for day in day_names:
        abbreviation_length = min(len(day), min_length)
        print(f"{abbreviation_length} {day}")

def process_day_names(file):
    with open(file, 'r') as f:
        day_names = f.read().splitlines()
    day_names = [day.upper() for day in day_names]
    return day_names

if __name__ == "__main__":
    day_names = process_day_names("days_of_week.txt")
    minimum_abbreviation_length(day_names, 3)
```