def my_sort(x):
    return ''.join(sorted(str(x), reverse=True))

def largest_int_v2(In):
    In = list(map(str, In))
    In.sort(key=my_sort, reverse=True)
    return int(''.join(In))