```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz(":- table p/2.")
prolog.assertz("p(N, X) :- X is N * (N + 1) // 2.")
prolog.assertz("p(N, X) :- X is N * (N - 1) // 2.")
prolog.assertz("p(N, X) :- between(1, N, I), J is I * I, X1 is J * J, X2 is X1 * X1, X3 is X2 * X2, X4 is X3 * X3, X5 is X4 * X4, X6 is X5 * X5, X7 is X6 * X6, X8 is X7 * X7, X is X8 + X7 + X6 + X5 + X4 + X3 + X2 + X1, !.")
result = list(prolog.query("p(6666, X)"))
print(result[0]["X"])
```