import ctypes

libc = ctypes.CDLL("libc.so.6")
result1 = libc.strcmp("abc", "def")
result2 = libc.strcmp("hello", "hello")

print(result1)  # Output: -1
print(result2)  # Output: 0