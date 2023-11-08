```python
import Prelude
import Debug.Trace

class ShortCircuit(Prelude):
    def __init__(self):
        super().__init__()

    def __and__(self, x, y):
        if not x:
            return False
        else:
            return y

    def __or__(self, x, y):
        if x:
            return True
        else:
            return y

def a(x):
    print("a:", x)
    return x

def b(x):
    print("b:", x)
    return x

def main():
    sc = ShortCircuit()
    p_values = [True, False]
    q_values = [True, False]
    results = [sc.p and sc.q for p in p_values for q in q_values]
    mapM_(print, results)

main()
```