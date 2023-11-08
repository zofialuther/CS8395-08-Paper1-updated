import datetime

# Get today's date
today = datetime.date.today()

# Get the ISO format of today's date
iso_format = today.isoformat()

# Format today's date in a specific way
formatted_date = today.strftime("%A, %B %d, %Y")

# Use positional arguments to format the date
positional_formatted_date = "The date is {0:%A, %B %d, %Y}".format(today)

# Use keyword arguments to format the date
keyword_formatted_date = "The date is {date:%A, %B %d, %Y}".format(date=today)

# Use f-strings to format the date
fstring_formatted_date = f"The date is {today:%A, %B %d, %Y}"