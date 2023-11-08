```python
import java.util.Calendar;
import java.util.GregorianCalendar;

public class Yuletide {
    public static void main(String[] args) {
        for (int year = 2008; year <= 2121; year++) {
            Calendar cal = new GregorianCalendar(year, Calendar.DECEMBER, 25);
            if (cal.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                System.out.println(year);
            }
        }
    }
}
```