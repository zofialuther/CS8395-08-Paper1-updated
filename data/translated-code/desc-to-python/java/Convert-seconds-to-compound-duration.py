def convert_seconds(seconds):
    output = ""
    weeks = seconds // (7*24*60*60)
    if weeks > 0:
        output += str(weeks) + " weeks, "
        seconds = seconds % (7*24*60*60)
    days = seconds // (24*60*60)
    if days > 0:
        output += str(days) + " days, "
        seconds = seconds % (24*60*60)
    hours = seconds // (60*60)
    if hours > 0:
        output += str(hours) + " hours, "
        seconds = seconds % (60*60)
    minutes = seconds // 60
    if minutes > 0:
        output += str(minutes) + " minutes, "
        seconds = seconds % 60
    if seconds > 0:
        output += str(seconds) + " seconds"
    return output.strip(", ")