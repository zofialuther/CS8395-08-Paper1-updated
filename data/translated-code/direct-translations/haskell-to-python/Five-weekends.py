```python
from datetime import date

def five_friday_months(y):
    months = []
    for m in range(1, 13):
        if date(y, m, 1).weekday() == 4 and date(y, m, 1).monthrange(y, m)[1] == 31:
            months.append((y, m))
    return months

def main():
    years = list(range(1900, 2101))
    xs = [five_friday_months(year) for year in years]
    lean = [year for months, year in zip(xs, years) if not months]
    n = sum([len(m) for m in xs])
    print("How many five-weekend months 1900-2100 ?")
    print("\t", n)
    print("First five ?")
    print("\t", xs[:5])
    print("Last five ?")
    print("\t", xs[-5:])
    print("How many lean years ? (No five-weekend months)")
    print("\t", len(lean))
    print("Which years are lean ?")
    for i in range(0, len(lean), 5):
        print("\t", " ".join(map(str, lean[i:i+5])))

if __name__ == "__main__":
    main()
```