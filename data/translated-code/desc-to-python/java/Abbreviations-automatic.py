```python
with open("days_of_week.txt", "r") as file:
    days = file.readlines()

abbreviations = {}

for day in days:
    day = day.strip()
    if day[:3] not in abbreviations.values():
        abbreviations[day] = day[:3]
    elif day[:2] not in abbreviations.values():
        abbreviations[day] = day[:2]
    elif day[:1] not in abbreviations.values():
        abbreviations[day] = day[:1]
    else:
        print(" ∞ ", day)

for day, abbreviation in abbreviations.items():
    print(len(abbreviation), day)
```