import datetime

# Using isoformat() method
current_date = datetime.date.today()
iso_formatted_date = current_date.isoformat()
print("ISO formatted date:", iso_formatted_date)

# Using strftime formatting codes
formatted_date = current_date.strftime("%A, %B %d, %Y")
print("Formatted date:", formatted_date)

# Using general string formatting system
general_formatted_date = "{:%A, %B %d, %Y}".format(current_date)
print("General formatted date:", general_formatted_date)

# Using f-strings for inline date formatting
inline_formatted_date = f"Today is {current_date:%A, %B %d, %Y}"
print("Inline formatted date:", inline_formatted_date)