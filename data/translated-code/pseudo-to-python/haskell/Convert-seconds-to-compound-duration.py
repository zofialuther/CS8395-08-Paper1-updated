def byUnits(rest, x):
    if x > 0:
        u, m = x, rest % x
    else:
        u, m = 1, rest
    return ((rest - m) // u, m)

def weekParts(daysPerWeek, hoursPerDay):
    return list(map(lambda x: x[0], mapAccumR(byUnits, 0, [0, daysPerWeek, hoursPerDay, 60, 60]))

def timeTags(numberLabelGap, pair, xs):
    n, s = pair
    if n > 0:
        return xs.append(interpolate(numberLabelGap, [str(n), s]))
    else:
        return xs

def durationString(componentGap, numberLabelGap, daysPerWeek, hoursPerDay, xs, n):
    return interpolate(componentGap, foldR(timeTags(numberLabelGap), [], zip(weekParts(daysPerWeek, hoursPerDay), xs, n)))

def translation(local, daysPerWeek, hoursPerDay, n):
    names = "wk d hr min sec"
    return interpolate("  ->  ", [str(n), durationString(", ", " ", daysPerWeek, hoursPerDay, words(local))])

def main():
    names = "wk d hr min sec"
    tests = [7259, 86400, 6000000]
    print("Assuming 24 hrs per day:")
    list(map(lambda x: print(translation(names, 7, 24, x)), tests))
    print("\nor, at 8 hours per day, 5 days per week:")
    list(map(lambda x: print(translation(names, 5, 8, x)), tests))