```python
def duration(seconds):
    weeks = seconds // 604800
    seconds = seconds % 604800
    days = seconds // 86400
    seconds = seconds % 86400
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"Weeks: {weeks}, Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

duration(7259)
duration(86400)
duration(6000000)
```