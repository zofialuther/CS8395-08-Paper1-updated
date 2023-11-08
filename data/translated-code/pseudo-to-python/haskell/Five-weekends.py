def fiveFridayMonths(y):
    monthsList = list(range(1, 13))
    result = []
    for m in monthsList:
        if isFriday(fromGregorian(y, m, 1)) and gregorianMonthLength(y, m) == 31:
            result.append((y, m))
    return result

def isFriday(d):
    weekDay = toWeekDate(d)
    return weekDay == 5

def main():
    years = list(range(1900, 2101))
    xs = list(map(fiveFridayMonths, years))
    lean = []
    for i in range(len(xs)):
        if not xs[i]:
            lean.append(years[i])
    n = len(flatten(xs))
    print("How many five-weekend months 1900-2100 ?")
    print("\t", n)
    print("First five ?")
    print("\t", take(5, flatten(xs)))
    print("Last five ?")
    print("\t", drop(n - 5, flatten(xs)))
    print("How many lean years ? (No five-weekend months)")
    print("\t", len(lean))
    print("Which years are lean ?")
    print(unlines(map(unwords, chunksOf(5, lean)))