import re

def rangeexpand(input_string):
    expanded_list = []
    ranges = input_string.split(',')
    
    for r in ranges:
        if '-' in r:
            start, end = map(int, r.split('-'))
            expanded_list.extend(range(start, end+1))
        else:
            expanded_list.append(int(r))
    
    return expanded_list