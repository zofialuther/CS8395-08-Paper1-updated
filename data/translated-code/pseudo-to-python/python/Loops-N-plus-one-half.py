from sys import stdout
write = stdout.write
n = 10
i = 1
while True:
    write(str(i))
    i += 1
    if i > n:
        break
    write(', ')