from datetime import datetime
import pytz

formats = [
    lambda t: t.strftime("%Y-%m-%d"),
    lambda t: t.strftime("%A, %B %d, %Y")
]

def main():
    current_time = datetime.now(pytz.utc).astimezone(pytz.timezone('America/New_York'))
    formatted_times = [f(current_time) for f in formats]
    print("\n".join(formatted_times))

main()