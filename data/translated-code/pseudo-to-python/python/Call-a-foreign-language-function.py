import ctypes
libc = ctypes.CDLL("/lib/libc.so.6")

# Compare two strings
def strcmp(s1, s2):
    result = libc.strcmp(s1.encode('utf-8'), s2.encode('utf-8'))
    if result < 0:
        return -1
    elif result > 0:
        return 1
    else:
        return 0

# Test cases
result1 = strcmp("abc", "def")     # -1
result2 = strcmp("hello", "hello") #  0