from sys import stdout

write = stdout.write
n, i = 10, 1

while True:
    write(str(i))
    i += 1
    if i > n:
        break
    write(', ')

# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10