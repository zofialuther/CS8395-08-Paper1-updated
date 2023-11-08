```python
def leap_year(L):
    leap_years, non_leap_years = partition(is_leap_year, L)
    print("Leap years:", format(leap_years))
    print("Non-leap years:", format(non_leap_years))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
```