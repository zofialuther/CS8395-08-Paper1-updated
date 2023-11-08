from datetime import datetime

millis = int(datetime.now().timestamp())
print("Current date and time in ISO 8601 format:", datetime.utcfromtimestamp(millis).isoformat())
print("Current date and time in custom format:", datetime.utcfromtimestamp(millis).strftime('%Y-%m-%d %H:%M:%S'))