```python
def fusc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return fusc(n//2)
    else:
        return fusc((n-1)//2) + fusc((n+1)//2)

def main():
    fusc_sequence = [fusc(i) for i in range(61)]
    for i, value in enumerate(fusc_sequence):
        print(f"Term {i}: {value}")
    
    print()
    
    for i in range(5):
        width = len(str(fusc_sequence[i]))
        print(f"Term {i}: {fusc_sequence[i]}, Width: {width}")

main()
```