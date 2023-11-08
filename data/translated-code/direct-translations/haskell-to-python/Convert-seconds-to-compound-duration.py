```python
from functools import reduce

def durationString(componentGap, numberLabelGap, daysPerWeek, hoursPerDay, xs, n):
    def timeTags(numberLabelGap, tup, xs):
        if tup[0] > 0:
            return [f"{tup[0]}{numberLabelGap}{tup[1]}"] + xs
        else:
            return xs
    
    def weekParts(daysPerWeek, hoursPerDay, n):
        def byUnits(rest, x):
            if x > 0:
                u, m = x, rest % x
            else:
                u, m = 1, rest
            return (rest - m) // u, m
        
        return list(reduce(lambda acc, x: byUnits(acc[1], x) , [0, daysPerWeek, hoursPerDay, 60, 60], initial=n))
    
    return componentGap.join([timeTags(numberLabelGap, x, []) for x in zip(weekParts(daysPerWeek, hoursPerDay, n), xs)])

def translation(local, daysPerWeek, hoursPerDay, n):
    def inner(n):
        return durationString(", ", " ", daysPerWeek, hoursPerDay, local.split(), n)
    
    return "  ->  ".join([str(n), inner(n)])

names = "wk d hr min sec"
tests = [7259, 86400, 6000000]

print("Assuming 24 hrs per day:")
for test in tests:
    print(translation(names, 7, 24, test))

print("\nor, at 8 hours per day, 5 days per week:")
for test in tests:
    print(translation(names, 5, 8, test))
```