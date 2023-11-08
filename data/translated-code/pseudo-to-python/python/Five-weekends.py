def five_weekends_per_month(start=START, stop=STOP):
    current_date = start
    last_month = weekend_days = 0
    five_weekends = []
    while current_date < stop:
        if current_date.month != last_month:
            if weekend_days >= 15:
                five_weekends.append(current_date - DAY)
            weekend_days = 0
            last_month = current_date.month
        if current_date.weekday() in WEEKEND:
            weekend_days += 1
        current_date += DAY
    return five_weekends

dates = five_weekends_per_month()
indent = '  '
print("There are " + str(len(dates)) + " months of which the first and last five are:")
print((indent + '\n' + indent).join(d.strftime(FMT) for d in dates[:5]))
print(indent + '...')
print(indent + (('\n' + indent).join(d.strftime(FMT) for d in dates[-5:]))

years_without_five_weekends_months = (STOP.year - START.year - len({d.year for d in dates}))
print("There are " + str(years_without_five_weekends_months) + " years in the range that do not have months with five weekends")