```python
from sys import stdout
write = stdout.write

n = 10
i = 1

while True:
    write(str(i))
    if i == n:
        break
    write(", ")
    i += 1
```