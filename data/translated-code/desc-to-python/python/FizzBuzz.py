```python
import itertools

fizz = itertools.cycle(["", "", "Fizz"])
buzz = itertools.cycle(["", "", "", "", "Buzz"])
fizz_buzz = (f or b for n, f, b in zip(range(1, 101), fizz, buzz))
print(list(itertools.islice(fizz_buzz, 100)))
```