def printCalendar(year, nCols):
    if nCols < 1 or nCols > 12:
        raise ValueError("Illegal column width.")
        
    date = datetime.date(year, 1, 1)
    nRows = math.ceil(12.0 / nCols)
    offs = date.weekday()
    w = nCols * 24
    monthNames = calendar.month_name[1:]
    mons = [[] for _ in range(12)]
    
    for m in range(12):
        name = monthNames[m]
        len = 11 + len(name) // 2
        format = "%{0}s%{1}s".format(len, 21 - len)
        mons[m][0] = format.format(name, "")
        mons[m][1] = " Su Mo Tu We Th Fr Sa"
        dim = calendar.monthrange(year, m+1)[1]
        
        for d in range(1, 44):
            isDay = d > offs and d <= offs + dim
            entry = " %2s".format(d - offs) if isDay else "   "
            if d % 7 == 1:
                mons[m][2 + (d - 1) // 7] = entry
            else:
                mons[m][2 + (d - 1) // 7] += entry
        offs = (offs + dim) % 7
        date = date.replace(month=date.month+1)
    
    print("Formatted string with Snoopy Picture and year")
    for r in range(nRows):
        for i in range(8):
            for c in range(r * nCols, (r + 1) * nCols):
                if c < 12:
                    print(mons[c][i])
            print("\n")
        print("\n")