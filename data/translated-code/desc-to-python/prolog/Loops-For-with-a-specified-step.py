```python
def for_loop(Hi, Lo, Step):
    if Step < 0 and Lo <= Hi:
        print(Hi)
        for_loop(Hi - Step, Lo, Step)
    else:
        return

for_loop(10, 1, 2)
```