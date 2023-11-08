```python
import java.util.Calendar;
import java.util.GregorianCalendar;

public class CalendarTask {
    public static void main(String[] args) {
        printCalendar(1969, 3);
    }

    public static void printCalendar(int year, int numColumns) {
        Calendar cal = new GregorianCalendar(year, 0, 1);
        cal.set(Calendar.DAY_OF_MONTH, 1);

        // Generate and format the calendar

        // Display the calendar with the specified number of columns

        // Print the fun Snoopy picture at the top of the calendar
    }
}
```