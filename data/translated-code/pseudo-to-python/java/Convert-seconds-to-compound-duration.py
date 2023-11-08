def duration(seconds):
    string = ""
    if seconds >= 604800:
        string += "{0} wk".format(int(seconds / 604800))
        seconds = seconds % 604800
    if seconds >= 86400:
        if string != "":
            string += ", "
        string += "{0} d".format(int(seconds / 86400))
        seconds = seconds % 86400
    if seconds >= 3600:
        if string != "":
            string += ", "
        string += "{0} hr".format(int(seconds / 3600))
        seconds = seconds % 3600
    if seconds >= 60:
        if string != "":
            string += ", "
        string += "{0} min".format(int(seconds / 60))
        seconds = seconds % 60
    if seconds > 0:
        if string != "":
            string += ", "
        string += "{0} sec".format(seconds)
    return string