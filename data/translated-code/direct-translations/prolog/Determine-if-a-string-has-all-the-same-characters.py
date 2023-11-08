```python
def main():
    same_or_different("")
    same_or_different("   ")
    same_or_different("2")
    same_or_different("333")
    same_or_different(".55")
    same_or_different("tttTTT")
    same_or_different("4444 444k")

def same_or_different(INPUTz0):
    print(f'input string is "{INPUTz0}" .')
    examine(INPUTz0)

def examine(INPUTz0, COMPARE0=None, INDEX0=1, INDEX=1):
    if not INPUTz0:
        print('all the same characters .')
    else:
        if COMPARE0 is None:
            COMPARE0 = INPUTz0[0]
        
        if COMPARE0 == INPUTz0[0]:
            INDEX0 += 1
            examine(INPUTz0[1:], COMPARE0, INDEX0, INDEX)
        else:
            DIFFERENT0 = INPUTz0[0]
            DIFFERENT_CODE = ord(DIFFERENT0)
            print(f'character "{DIFFERENT0}" (hex {DIFFERENT_CODE:02x}) different than "{COMPARE0}" at 1-based index {INDEX} .')

main()
```