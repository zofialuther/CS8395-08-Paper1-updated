def duration(seconds):
    string = ""
    if seconds >= 604800:  # 1 wk
        string += "{:d} wk".format(seconds // 604800)
        seconds %= 604800
    if seconds >= 86400:  # 1 d
        if string:
            string += ", "
        string += "{:d} d".format(seconds // 86400)
        seconds %= 86400
    if seconds >= 3600:  # 1 hr
        if string:
            string += ", "
        string += "{:d} hr".format(seconds // 3600)
        seconds %= 3600
    if seconds >= 60:  # 1 min
        if string:
            string += ", "
        string += "{:d} min".format(seconds // 60)
        seconds %= 60
    if seconds > 0:
        if string:
            string += ", "
        string += "{:d} sec".format(seconds)
    return string