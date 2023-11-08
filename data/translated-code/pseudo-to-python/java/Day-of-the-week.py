import java.util.Calendar
import java.util.Date
import java.util.GregorianCalendar

class Yuletide:
    def main():
        calendar = Calendar.getInstance()
        count = 1
        for year in range(2008, 2122):
            calendar.set(year, Calendar.DECEMBER, 25)
            if calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY:
                if count != 1:
                    print(", ", end="")
                print(year, end="")
                count += 1

Yuletide.main()