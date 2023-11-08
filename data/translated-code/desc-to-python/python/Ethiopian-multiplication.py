```python
def ethMult(n, m):
    result = 0
    while n > 0:
        if n % 2 != 0:
            result += m
        n = n // 2
        m = m * 2
    return result

def double(num):
    return num * 2

def halve(num):
    return num // 2

def addIfOdd(num, addend):
    if num % 2 != 0:
        return num + addend
    else:
        return num

def iterate(func, start, times):
    result = start
    for i in range(times):
        result = func(result)
    return result

def showLogs(logs):
    for log in logs:
        print(log)

def unfold(func, start, end):
    result = []
    for i in range(start, end+1):
        result.append(func(i))
    return result

def main():
    n = 17
    m = 23
    print(ethMult(n, m))

if __name__ == "__main__":
    main()
```