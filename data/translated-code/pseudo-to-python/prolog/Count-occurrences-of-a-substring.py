def count_substring(String, Sub, Total):
    count_substring_helper(String, Sub, 0, Total)

def count_substring_helper(String, Sub, Count, Total):
    if substring_rest(String, Sub, Rest):
        NextCount = Count + 1
        count_substring_helper(Rest, Sub, NextCount, Total)
    else:
        Total = Count

def substring_rest(String, Sub, Rest):
    Before, Length, Remain = sub_string(String, Sub)
    DropN = Before + Length
    Rest = String[DropN:]

def sub_string(String, Sub):
    if Sub in String:
        Before = String.index(Sub)
        Length = len(Sub)
        Remain = len(String) - (Before + Length)
        return Before, Length, Remain
    else:
        return -1, -1, -1