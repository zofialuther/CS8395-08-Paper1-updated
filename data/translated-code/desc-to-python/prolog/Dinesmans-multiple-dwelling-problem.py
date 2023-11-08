```python
from pyswip import Prolog, Functor, Variable, Query

prolog = Prolog()

def init():
    prolog.assertz((0 < Baker) & (Baker < 5))
    prolog.assertz((0 < Cooper) & (Cooper < 5))
    prolog.assertz((0 < Fletcher) & (Fletcher < 5))
    prolog.assertz((0 < Miller) & (Miller < 5))
    prolog.assertz((0 < Smith) & (Smith < 5))
    prolog.assertz(Baker > Cooper)
    prolog.assertz(Fletcher > Cooper)
    prolog.assertz(abs(Miller - Smith) > 1)
    prolog.assertz(abs(Fletcher - Smith) > 1)
    prolog.assertz(abs(Fletcher - Cooper) > 1)

def solve():
    solutions = prolog.query((Baker, Cooper, Fletcher, Miller, Smith))
    for sol in solutions:
        print(sol)

def dinners():
    init()
    solve()

dinners()
```