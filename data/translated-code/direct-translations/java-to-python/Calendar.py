from calendar import Calendar, month_name
import math

class CalendarTask:
    def main(self):
        self.print_calendar(1969, 3)

    def print_calendar(self, year, nCols):
        if nCols < 1 or nCols > 12:
            raise ValueError("Illegal column width.")

        date = Calendar()
        date.setyear(year)
        date.setmonth(1)
        date.setday(1)
        
        nRows = math.ceil(12.0 / nCols)
        offs = date.weekday()
        w = nCols * 24

        monthNames = month_name[1:]

        mons = [["" for _ in range(8)] for _ in range(12)]
        for m in range(12):
            name = monthNames[m]
            len = 11 + len(name) // 2
            format = f"%{len}s%{21 - len}s"

            mons[m][0] = f"{name.center(len)}".ljust(21 - len)
            mons[m][1] = " Su Mo Tu We Th Fr Sa"
            dim = date.monthrange(year, m + 1)[1]

            for d in range(1, 43):
                isDay = d > offs and d <= offs + dim
                entry = f" {d - offs:02}" if isDay else "   "
                if d % 7 == 1:
                    mons[m][2 + (d - 1) // 7] = entry
                else:
                    mons[m][2 + (d - 1) // 7] += entry
            offs = (offs + dim) % 7
            date.setmonth(m + 2)

        print(f"{'[Snoopy Picture]'.center(w // 2 + 10)}")
        print(f"{year}".center(w // 2 + 4), "\n")

        for r in range(nRows):
            for i in range(8):
                for c in range(r * nCols, min((r + 1) * nCols, 12)):
                    print(f"   {' '.join(mons[c][i])}", end="")
                print()
            print()