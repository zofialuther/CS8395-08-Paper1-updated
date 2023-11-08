```python
from Control.Monad.Fix import fix

def spam_loop():
    fix(lambda action: putStrLn("SPAM") >> action)
```