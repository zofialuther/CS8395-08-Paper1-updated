```python
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("item(apple, 50, 10)")
prolog.assertz("item(book, 200, 100)")
prolog.assertz("item(pen, 20, 5)")
prolog.assertz("item(laptop, 3000, 500)")
prolog.assertz("item(phone, 500, 200)")

prolog.assertz("knapsack_limit(400)")

for soln in prolog.query("item(Name, Weight, Value), knapsack_limit(Limit), X in 0..1, Weight*X #=< Limit, findall((Name, Weight, Value, X), item(Name, Weight, Value), Items), maximize(labeling([max(Value)], Items), Value)"):
    print(soln)
```