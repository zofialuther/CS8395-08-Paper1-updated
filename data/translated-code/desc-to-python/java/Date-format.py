```python
import datetime

# Get current system time in milliseconds
current_time_millis = datetime.datetime.now().timestamp()

# Convert milliseconds to seconds
current_time_seconds = current_time_millis / 1000

# Convert seconds to date
date = datetime.datetime.fromtimestamp(current_time_seconds)

# Print date in "YYYY-MM-DD" format
print(date.strftime("%Y-%m-%d"))

# Print date in "Day of the week, Month Day, Year" format
print(date.strftime("%A, %B %d, %Y"))
```