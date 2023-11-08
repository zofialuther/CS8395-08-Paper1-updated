def count_substring(String, Sub, Total):
    count_substring(String, Sub, 0, Total)

def count_substring(String, Sub, Count, Total):
    if substring_rest(String, Sub, Rest):
        NextCount = Count + 1
        count_substring(Rest, Sub, NextCount, Total)
    else:
        Total = Count

def substring_rest(String, Sub, Rest):
    Before, Length, Remain = String.index(Sub), len(Sub), len(String) - String.index(Sub) - len(Sub)
    Rest = String[Before + Length:]
    return Rest