import ctypes

libc = ctypes.CDLL("/lib/libc.so.6")

print(libc.strcmp("abc", "def"))     # -1
print(libc.strcmp("hello", "hello")) #  0