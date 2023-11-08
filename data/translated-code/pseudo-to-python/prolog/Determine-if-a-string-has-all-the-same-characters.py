```python
def main():
    same_or_different("")
    same_or_different(" ")
    same_or_different("2")
    same_or_different("333")
    same_or_different(".55")
    same_or_different("tttTTT")
    same_or_different("4444 444k")

def same_or_different(INPUTz0):
    print(f"Input string: {INPUTz0}")
    examine(INPUTz0)

def examine(INPUTz0, COMPARE0="", INDEX0=0, INDEX=0):
    if len(INPUTz0) == 0:
        print("All the same characters")
    else:
        examine(INPUTz0[1:], INPUTz0[0])

def examine(INPUTz0, COMPARE0, INDEX0, INDEX):
    if len(INPUTz0) == 0:
        print("All the same characters")
    elif INPUTz0[0] == COMPARE0:
        INDEX0 += 1
        examine(INPUTz0[1:], COMPARE0, INDEX0, INDEX)
    else:
        print(f"Different character: {INPUTz0[0]}, Code: {ord(INPUTz0[0])}, Compared character: {COMPARE0}, Index: {INDEX}")
```