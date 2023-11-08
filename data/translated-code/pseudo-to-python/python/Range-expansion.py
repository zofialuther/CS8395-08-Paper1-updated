import re

def rangeexpand(txt):
    lst = []
    ranges = txt.split(',')
    for r in ranges:
        match = re.match(r'(\d+)-(\d+)', r)
        if match:
            start = int(match.group(1))
            end = int(match.group(2))
            lst.extend(range(start, end+1))
        else:
            lst.append(int(r))
    return lst