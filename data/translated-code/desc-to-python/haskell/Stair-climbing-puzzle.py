```python
def stepUp(step, test):
    def untilM(action):
        if test():
            return action
        else:
            return untilM(step >> action)
    return untilM(identity)
```